// AI Web Novel Reader & Translator Frontend Application

// Global fetch interceptor to append X-App-Passcode header
const _originalFetch = window.fetch;
window.fetch = async function(...args) {
  let [resource, config] = args;
  config = config || {};
  config.headers = config.headers || {};
  const passcode = localStorage.getItem('novel_app_passcode') || sessionStorage.getItem('novel_app_passcode');
  if (passcode) {
    if (config.headers instanceof Headers) {
      config.headers.set('X-App-Passcode', passcode);
    } else {
      config.headers['X-App-Passcode'] = passcode;
    }
  }
  const response = await _originalFetch(resource, config);
  if (response.status === 401 && typeof resource === 'string' && resource.startsWith('/api/') && !resource.startsWith('/api/auth/')) {
    window.dispatchEvent(new CustomEvent('novel-auth-required'));
  }
  return response;
};

const { createApp, ref, reactive, computed, onMounted, onUnmounted, watch, nextTick } = Vue;

const app = createApp({
  setup() {
    // Auth & Private Single-User Lock State
    const isAppLocked = ref(false);
    const isAuthChecking = ref(true);
    const authRequiresPasscode = ref(false);
    const isEnvLocked = ref(false);
    const inputPasscode = ref('');
    const rememberDevice = ref(true);
    const authError = ref('');
    const newPasscode = ref('');
    const oldPasscode = ref('');

    // Navigation & View State
    const currentView = ref('library'); // library, detail, reader, glossary, settings
    const selectedNovelId = ref(null);
    const selectedNovel = ref(null);
    const currentChapter = ref(null);
    const novels = ref([]);
    const chapters = ref([]);
    const chapterSearch = ref('');
    const chapterFilter = ref('all'); // all, completed, pending
    const librarySearch = ref('');
    const isLoading = ref(false);
    const isTranslating = ref(false);
    const streamingText = ref('');
    const toast = reactive({ show: false, message: '', type: 'info' });

    // Modals & Drawers
    const showAddModal = ref(false);
    const addTab = ref('url'); // url, raw
    const showBatchModal = ref(false);
    const showSettingsModal = ref(false);
    const showTocDrawer = ref(false);
    const showGlossaryExtractModal = ref(false);
    const showAddGlossaryModal = ref(false);
    const showEditRuleModal = ref(false);

    // Online Discover State
    const activeMainTab = ref('library'); // 'library' | 'discover'
    const discoverCategories = ref([]);
    const selectedDiscoverCategory = ref('all');
    const selectedSourceMode = ref('all'); // 'all', 'curated', 'live'
    const discoverSort = ref('hot'); // 'hot', 'views', 'rating', 'chapters'
    const discoverTimeRange = ref('all'); // 'all', 'week', 'month', 'year'
    const discoverSearch = ref('');
    const discoverNovels = ref([]);
    const discoverPage = ref(1);
    const discoverTotal = ref(0);
    const discoverHasMore = ref(false);
    const isDiscoverLoading = ref(false);
    const isDiscoverLoadingMore = ref(false);
    const cloningNovelId = ref(null);
    const previewNovel = ref(null);
    const showPreviewModal = ref(false);

    // Reader UI & Theme Settings
    const showReaderControls = ref(true);
    const isBilingual = ref(false);
    const isShowingRawFallback = ref(false);
    const isFullscreen = ref(false);
    const readingProgress = ref(0);
    const isChapterAnimate = ref(true);
    let lastScrollY = 0;

    // Unconditionally set 100% full width layout (never allow narrow 750/850/900 margins)
    localStorage.setItem('reader_max_width', '100%');
    const readerSettings = reactive({
      theme: localStorage.getItem('reader_theme') || 'theme-dark',
      font: localStorage.getItem('reader_font') || 'font-literata',
      fontSize: parseInt(localStorage.getItem('reader_font_size') || '18'),
      lineHeight: parseFloat(localStorage.getItem('reader_line_height') || '1.8'),
      maxWidth: '100%',
      sidePadding: localStorage.getItem('reader_side_padding') || 'compact', // 'tight', 'compact', 'normal'
    });

    // Add Novel Forms
    const novelUrlForm = reactive({
      url: '',
      auto_detect: true,
      max_chapters: null
    });
    const novelRawForm = reactive({
      title: '',
      author: 'Chưa rõ',
      description: '',
      raw_text: ''
    });

    // Batch Translation Form
    const batchForm = reactive({
      start_index: 1,
      count: 20,
      all_remaining: false,
      concurrency: 2
    });

    // Bulk Download / Scrape Form
    const showBulkDownloadModal = ref(false);
    const bulkDownloadLoading = ref(false);
    const bulkDownloadForm = reactive({
      start_index: 1,
      count: 100,
      all_remaining: false
    });
    const scrapeStatus = ref(null);
    let scrapePollTimer = null;

    // AI Settings
    const aiSettings = reactive({
      api_base_url: 'https://generativelanguage.googleapis.com/v1beta/openai/',
      api_key: '',
      model_name: 'gemini-2.5-flash',
      temperature: 0.3,
      system_prompt: ''
    });
    const availableModels = ref([]);
    const isTestingAi = ref(false);
    const aiTestResult = ref(null);

    // Glossary State
    const glossaryItems = ref([]);
    const glossaryCategory = ref('all');
    const glossarySearch = ref('');
    const glossaryForm = reactive({
      id: null,
      source_term: '',
      target_term: '',
      category: 'nhan_vat',
      notes: ''
    });
    const glossarySuggestions = ref([]);
    const selectedSuggestions = ref([]);
    const isExtractingGlossary = ref(false);

    // Scraper Rules State
    const scraperRules = ref([]);
    const currentRule = reactive({
      id: null,
      domain: '',
      name: '',
      novel_title_selector: '',
      novel_author_selector: '',
      novel_cover_selector: '',
      novel_desc_selector: '',
      chapter_list_selector: '',
      chapter_link_selector: '',
      chapter_title_selector: '',
      chapter_content_selector: '',
      content_remove_selectors: 'script,style,ins,ads,.ads,#ads,.advertisement',
      encoding: 'auto'
    });

    // Toast Notification helper
    function showToast(message, type = 'info', duration = 3000) {
      toast.message = message;
      toast.type = type;
      toast.show = true;
      setTimeout(() => { toast.show = false; }, duration);
    }

    // Save reader settings to localStorage
    function updateReaderSetting(key, val) {
      readerSettings[key] = val;
      localStorage.setItem(`reader_${key}`, val);
    }

    // --- API Calls ---

    // 1. Fetch Novels
    async function loadNovels() {
      isLoading.value = true;
      try {
        const res = await fetch('/api/novels');
        novels.value = await res.json();
      } catch (err) {
        showToast('Không thể tải danh sách truyện', 'error');
      } finally {
        isLoading.value = false;
      }
    }

    // 2. Open Novel Detail
    async function openNovelDetail(novelId) {
      selectedNovelId.value = novelId;
      isLoading.value = true;
      try {
        const [nRes, cRes] = await Promise.all([
          fetch(`/api/novels/${novelId}`),
          fetch(`/api/novels/${novelId}/chapters?limit=5000`)
        ]);
        selectedNovel.value = await nRes.json();
        chapters.value = await cRes.json();
        currentView.value = 'detail';
        window.scrollTo(0, 0);
        loadScrapeStatus(novelId);
      } catch (err) {
        showToast('Không thể tải thông tin truyện', 'error');
      } finally {
        isLoading.value = false;
      }
    }

    // 3. Add Novel from URL
    async function submitNovelUrl() {
      if (!novelUrlForm.url.trim()) {
        showToast('Vui lòng nhập đường link truyện', 'warning');
        return;
      }
      isLoading.value = true;
      try {
        const res = await fetch('/api/novels/scrape', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(novelUrlForm)
        });
        if (!res.ok) {
          const err = await res.json();
          throw new Error(err.detail || 'Lỗi khi cào truyện');
        }
        const created = await res.json();
        showToast(`Đã thêm truyện: ${created.title} (${created.total_chapters} chương)`, 'success');
        showAddModal.value = false;
        novelUrlForm.url = '';
        await loadNovels();
        await openNovelDetail(created.id);
      } catch (err) {
        showToast(err.message, 'error', 5000);
      } finally {
        isLoading.value = false;
      }
    }

    // 4. Add Novel from Raw Text
    async function submitNovelRaw() {
      if (!novelRawForm.title.trim() || !novelRawForm.raw_text.trim()) {
        showToast('Vui lòng nhập tên truyện và nội dung tiếng Trung', 'warning');
        return;
      }
      isLoading.value = true;
      try {
        const res = await fetch('/api/novels/raw', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(novelRawForm)
        });
        if (!res.ok) {
          const err = await res.json();
          throw new Error(err.detail || 'Lỗi khi nhập truyện');
        }
        const created = await res.json();
        showToast(`Đã tạo truyện: ${created.title} (${created.total_chapters} chương)`, 'success');
        showAddModal.value = false;
        novelRawForm.title = '';
        novelRawForm.raw_text = '';
        await loadNovels();
        await openNovelDetail(created.id);
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        isLoading.value = false;
      }
    }

    // 5. Upload .TXT File
    async function handleFileUpload(e) {
      const file = e.target.files[0];
      if (!file) return;

      const formData = new FormData();
      formData.append('title', file.name.replace(/\.[^/.]+$/, ''));
      formData.append('author', 'Chưa rõ');
      formData.append('description', `Tải lên từ file: ${file.name}`);
      formData.append('file', file);

      isLoading.value = true;
      try {
        const res = await fetch('/api/novels/upload', {
          method: 'POST',
          body: formData
        });
        if (!res.ok) {
          const err = await res.json();
          throw new Error(err.detail || 'Lỗi khi tải lên file');
        }
        const created = await res.json();
        showToast(`Tải lên thành công: ${created.title} (${created.total_chapters} chương)`, 'success');
        showAddModal.value = false;
        await loadNovels();
        await openNovelDetail(created.id);
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        isLoading.value = false;
      }
    }

    // 6. Delete Novel
    async function deleteNovel(novelId, title) {
      if (!confirm(`Bạn có chắc muốn xóa truyện "${title}" không?`)) return;
      try {
        const res = await fetch(`/api/novels/${novelId}`, { method: 'DELETE' });
        if (res.ok) {
          showToast('Đã xóa truyện', 'success');
          if (currentView.value === 'detail') currentView.value = 'library';
          await loadNovels();
        }
      } catch (err) {
        showToast('Lỗi khi xóa truyện', 'error');
      }
    }

    // 7. Open Chapter in Reader
    async function openChapter(chapterId) {
      isLoading.value = true;
      isChapterAnimate.value = false;
      streamingText.value = '';
      try {
        const res = await fetch(`/api/chapters/${chapterId}?prefetch=true`);
        if (!res.ok) throw new Error('Không thể tải chương');
        currentChapter.value = await res.json();
        currentView.value = 'reader';
        showTocDrawer.value = false;
        readingProgress.value = 0;

        // Sync read progress to server
        syncReadingProgress(currentChapter.value.novel_id, currentChapter.value.id, currentChapter.value.chapter_index);

        // Restore scroll position after DOM renders
        await nextTick();
        window.scrollTo({ top: 0, behavior: 'instant' });
        isShowingRawFallback.value = false;

        // Trigger smooth chapter enter animation
        setTimeout(() => {
          isChapterAnimate.value = true;
        }, 50);
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        isLoading.value = false;
      }
    }

    // 8. Stream Translation
    async function startStreamTranslation(chapterId, force = false) {
      if (isTranslating.value) return;
      isTranslating.value = true;
      streamingText.value = '';

      try {
        const response = await fetch(`/api/chapters/${chapterId}/stream?force=${force}`);
        const reader = response.body.getReader();
        const decoder = new TextDecoder('utf-8');
        let buffer = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split('\n');
          buffer = lines.pop(); // keep last incomplete line

          for (const line of lines) {
            if (line.startsWith('data:')) {
              const jsonStr = line.substring(5).trim();
              if (jsonStr) {
                try {
                  const data = JSON.parse(jsonStr);
                  if (data.error) {
                    showToast(`Lỗi dịch: ${data.error}`, 'error', 4000);
                  } else if (data.chunk) {
                    streamingText.value += data.chunk;
                  } else if (data.done) {
                    if (data.title_translated && currentChapter.value) {
                      currentChapter.value.title_translated = data.title_translated;
                    }
                    if (currentChapter.value) {
                      currentChapter.value.translated_content = streamingText.value;
                      currentChapter.value.translation_status = 'completed';
                    }
                  }
                } catch (e) {
                  console.error('SSE JSON error', e);
                }
              }
            }
          }
        }
      } catch (err) {
        showToast(`Lỗi trong luồng dịch: ${err.message}`, 'error');
      } finally {
        isTranslating.value = false;
        streamingText.value = '';
        // Reload chapter state
        if (currentChapter.value) {
          const r = await fetch(`/api/chapters/${currentChapter.value.id}?prefetch=false`);
          currentChapter.value = await r.json();
        }
      }
    }

    async function requestAntigravityTranslation(ch, count = 1) {
      if (!ch) return;
      const cmd = `Dịch tiếp chương ${ch.chapter_index} truyện ${ch.novel_title || ''}`;
      try {
        await fetch('/api/queue/request', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            novel_id: ch.novel_id,
            chapter_index: ch.chapter_index,
            chapter_count: count,
            novel_title: ch.novel_title || ''
          })
        });
      } catch (e) {
        console.warn('Lỗi gửi hàng đợi:', e);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(cmd).catch(() => {});
      }
      showToast(`✅ Đã gửi lệnh dịch Chương ${ch.chapter_index} vào hàng đợi! Lệnh '${cmd}' đã được tự động copy vào clipboard.`, 'success', 5000);
    }

    async function openNovelPreview(novel) {
      previewNovel.value = novel;
      showPreviewModal.value = true;
      try {
        const res = await fetch(`/api/discover/novel/${novel.id}`);
        if (res.ok) {
          previewNovel.value = await res.json();
        }
      } catch (e) {
        console.warn('Lỗi tải chi tiết truyện:', e);
      }
    }

    function closeNovelPreview() {
      showPreviewModal.value = false;
      previewNovel.value = null;
    }

    // 9. Sync Reading Progress (Debounced)
    let syncTimeout = null;
    function syncReadingProgress(novelId, chapterId, chapterIndex, scrollPos = 0) {
      if (syncTimeout) clearTimeout(syncTimeout);
      syncTimeout = setTimeout(async () => {
        try {
          await fetch(`/api/novels/${novelId}/progress`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              last_read_chapter_id: chapterId,
              last_read_index: chapterIndex,
              scroll_position: scrollPos
            })
          });
        } catch (e) {
          console.warn('Sync reading progress failed:', e);
        }
      }, 1000);
    }

    // 10. Batch Translate
    async function submitBatchTranslate() {
      if (!selectedNovel.value) return;
      try {
        const res = await fetch(`/api/novels/${selectedNovel.value.id}/batch-translate`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(batchForm)
        });
        const data = await res.json();
        showToast(data.message, 'success', 5000);
        showBatchModal.value = false;

        // Auto copy Antigravity prompt to clipboard
        const cmd = batchForm.all_remaining
          ? `Dịch toàn bộ các chương còn lại của truyện ${selectedNovel.value.title}`
          : `Dịch tiếp ${batchForm.count} chương truyện ${selectedNovel.value.title} từ chương ${batchForm.start_index}`;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(cmd).catch(() => {});
        }

        // Refresh chapters
        await openNovelDetail(selectedNovel.value.id);
      } catch (err) {
        showToast('Lỗi khi kích hoạt dịch hàng loạt', 'error');
      }
    }

    // 10b. Bulk Scrape & Export TXT
    async function loadScrapeStatus(novelId) {
      if (!novelId) return;
      try {
        const res = await fetch(`/api/novels/${novelId}/scrape-status`);
        if (res.ok) {
          scrapeStatus.value = await res.json();
          if (scrapeStatus.value.is_scraping && !scrapePollTimer) {
            scrapePollTimer = setInterval(() => {
              if (selectedNovel.value && selectedNovel.value.id === novelId) {
                loadScrapeStatus(novelId);
              } else {
                clearInterval(scrapePollTimer);
                scrapePollTimer = null;
              }
            }, 2500);
          } else if (!scrapeStatus.value.is_scraping && scrapePollTimer) {
            clearInterval(scrapePollTimer);
            scrapePollTimer = null;
            // Scrape completed, reload chapters
            const cRes = await fetch(`/api/novels/${novelId}/chapters?limit=5000`);
            if (cRes.ok) chapters.value = await cRes.json();
          }
        }
      } catch (e) {
        console.warn('Failed to load scrape status:', e);
      }
    }

    function openBulkDownloadModal() {
      if (!selectedNovel.value) return;
      showBulkDownloadModal.value = true;
      loadScrapeStatus(selectedNovel.value.id);
    }

    async function submitBulkDownload() {
      if (!selectedNovel.value) return;
      bulkDownloadLoading.value = true;
      try {
        const res = await fetch(`/api/novels/${selectedNovel.value.id}/bulk-scrape`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(bulkDownloadForm)
        });
        const data = await res.json();
        if (res.ok) {
          showToast(data.message || 'Đã khởi chạy tác vụ tải nội dung...', 'info', 4000);
          await loadScrapeStatus(selectedNovel.value.id);
        } else {
          showToast(data.detail || 'Lỗi khi bắt đầu tải', 'error');
        }
      } catch (err) {
        showToast('Lỗi mạng: ' + err.message, 'error');
      } finally {
        bulkDownloadLoading.value = false;
      }
    }

    function exportNovelTxt(mode = 'translated') {
      if (!selectedNovel.value) return;
      const url = `/api/novels/${selectedNovel.value.id}/export?mode=${mode}`;
      window.open(url, '_blank');
    }

    // 11. AI Entity/Glossary Extraction
    async function triggerExtractGlossary() {
      if (!currentChapter.value) return;
      isExtractingGlossary.value = true;
      showGlossaryExtractModal.value = true;
      glossarySuggestions.value = [];
      selectedSuggestions.value = [];

      try {
        const res = await fetch(`/api/chapters/${currentChapter.value.id}/extract-glossary`, {
          method: 'POST'
        });
        if (!res.ok) throw new Error('Không thể trích xuất thực thể');
        const data = await res.json();
        glossarySuggestions.value = data;
        selectedSuggestions.value = data.map((_, i) => i);
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        isExtractingGlossary.value = false;
      }
    }

    async function applySelectedGlossarySuggestions() {
      if (!selectedNovelId.value && currentChapter.value) {
        selectedNovelId.value = currentChapter.value.novel_id;
      }
      const itemsToImport = selectedSuggestions.value.map(idx => glossarySuggestions.value[idx]);
      if (itemsToImport.length === 0) {
        showToast('Vui lòng chọn ít nhất 1 từ', 'warning');
        return;
      }

      try {
        const res = await fetch(`/api/novels/${selectedNovelId.value}/glossary/bulk`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ items: itemsToImport })
        });
        const result = await res.json();
        showToast(`Đã thêm thành công ${result.added} từ vào Từ điển`, 'success');
        showGlossaryExtractModal.value = false;
      } catch (err) {
        showToast('Lỗi khi lưu từ điển', 'error');
      }
    }

    // 12. Glossary CRUD
    async function loadGlossary(novelId) {
      try {
        let url = `/api/novels/${novelId}/glossary?category=${glossaryCategory.value}`;
        if (glossarySearch.value) url += `&search=${encodeURIComponent(glossarySearch.value)}`;
        const res = await fetch(url);
        glossaryItems.value = await res.json();
      } catch (err) {
        showToast('Lỗi tải từ điển', 'error');
      }
    }

    async function saveGlossaryItem() {
      if (!glossaryForm.source_term.trim() || !glossaryForm.target_term.trim()) {
        showToast('Vui lòng nhập từ gốc và từ dịch', 'warning');
        return;
      }

      try {
        if (glossaryForm.id) {
          await fetch(`/api/glossary/${glossaryForm.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(glossaryForm)
          });
          showToast('Đã cập nhật từ', 'success');
        } else {
          await fetch(`/api/novels/${selectedNovelId.value}/glossary`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(glossaryForm)
          });
          showToast('Đã thêm từ mới', 'success');
        }
        showAddGlossaryModal.value = false;
        glossaryForm.id = null;
        glossaryForm.source_term = '';
        glossaryForm.target_term = '';
        glossaryForm.notes = '';
        await loadGlossary(selectedNovelId.value);
      } catch (err) {
        showToast('Lỗi khi lưu từ', 'error');
      }
    }

    async function deleteGlossaryItem(id) {
      if (!confirm('Xóa từ này khỏi từ điển?')) return;
      try {
        await fetch(`/api/glossary/${id}`, { method: 'DELETE' });
        showToast('Đã xóa', 'success');
        await loadGlossary(selectedNovelId.value);
      } catch (err) {
        showToast('Lỗi khi xóa từ', 'error');
      }
    }

    function openEditGlossary(item) {
      glossaryForm.id = item.id;
      glossaryForm.source_term = item.source_term;
      glossaryForm.target_term = item.target_term;
      glossaryForm.category = item.category;
      glossaryForm.notes = item.notes;
      showAddGlossaryModal.value = true;
    }

    // 13. AI Settings & Model Discovery
    async function loadSettings() {
      try {
        const res = await fetch('/api/settings');
        const data = await res.json();
        Object.assign(aiSettings, data);
      } catch (err) {
        console.warn('Lỗi tải settings:', err);
      }
    }

    async function saveSettings() {
      try {
        await fetch('/api/settings', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(aiSettings)
        });
        showToast('Đã lưu cài đặt AI', 'success');
        showSettingsModal.value = false;
      } catch (err) {
        showToast('Lỗi khi lưu cài đặt', 'error');
      }
    }

    async function fetchAiModels() {
      try {
        showToast('Đang kết nối lấy model...', 'info');
        const url = `/api/settings/models?base_url=${encodeURIComponent(aiSettings.api_base_url)}&api_key=${encodeURIComponent(aiSettings.api_key || '')}`;
        const res = await fetch(url);
        const data = await res.json();
        if (data.models && data.models.length > 0) {
          availableModels.value = data.models;
          showToast(`Tìm thấy ${data.models.length} model`, 'success');
          if (!data.models.includes(aiSettings.model_name)) {
            aiSettings.model_name = data.models[0];
          }
        } else {
          showToast('Không có model nào trả về từ API', 'warning');
        }
      } catch (err) {
        showToast('Không thể kết nối đến AI Base URL', 'error');
      }
    }

    async function testAiConnection() {
      isTestingAi.value = true;
      aiTestResult.value = null;
      try {
        const res = await fetch('/api/settings/test', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            api_base_url: aiSettings.api_base_url,
            api_key: aiSettings.api_key,
            model_name: aiSettings.model_name,
            test_prompt: 'Xin chào, bạn đã sẵn sàng dịch tiểu thuyết chưa?'
          })
        });
        aiTestResult.value = await res.json();
      } catch (err) {
        aiTestResult.value = { status: 'error', message: err.message };
      } finally {
        isTestingAi.value = false;
      }
    }

    // 14. Scraper Rules
    async function loadScraperRules() {
      try {
        const res = await fetch('/api/scraper-rules');
        scraperRules.value = await res.json();
      } catch (err) {
        console.warn('Lỗi tải scraper rules:', err);
      }
    }

    async function saveRule() {
      try {
        const method = currentRule.id ? 'PUT' : 'POST';
        const url = currentRule.id ? `/api/scraper-rules/${currentRule.id}` : '/api/scraper-rules';
        const res = await fetch(url, {
          method,
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(currentRule)
        });
        if (!res.ok) {
          const e = await res.json();
          throw new Error(e.detail || 'Lỗi lưu quy tắc');
        }
        showToast('Đã lưu quy tắc cào', 'success');
        showEditRuleModal.value = false;
        await loadScraperRules();
      } catch (err) {
        showToast(err.message, 'error');
      }
    }

    async function deleteRule(id) {
      if (!confirm('Xóa quy tắc domain này?')) return;
      try {
        await fetch(`/api/scraper-rules/${id}`, { method: 'DELETE' });
        showToast('Đã xóa quy tắc', 'success');
        await loadScraperRules();
      } catch (err) {
        showToast('Lỗi khi xóa', 'error');
      }
    }

    function openEditRule(rule = null) {
      if (rule) {
        Object.assign(currentRule, rule);
      } else {
        currentRule.id = null;
        currentRule.domain = '';
        currentRule.name = '';
        currentRule.novel_title_selector = '';
        currentRule.novel_author_selector = '';
        currentRule.novel_cover_selector = '';
        currentRule.novel_desc_selector = '';
        currentRule.chapter_list_selector = '';
        currentRule.chapter_link_selector = '';
        currentRule.chapter_title_selector = '';
        currentRule.chapter_content_selector = '';
        currentRule.content_remove_selectors = 'script,style,ins,ads,.ads,#ads,.advertisement';
        currentRule.encoding = 'auto';
      }
      showEditRuleModal.value = true;
    }

    // --- Computed Values ---
    const filteredNovels = computed(() => {
      if (!librarySearch.value.trim()) return novels.value;
      const q = librarySearch.value.toLowerCase();
      return novels.value.filter(n =>
        n.title.toLowerCase().includes(q) || (n.author && n.author.toLowerCase().includes(q))
      );
    });

    const filteredChapters = computed(() => {
      let list = chapters.value;
      if (chapterFilter.value === 'completed') {
        list = list.filter(c => c.translation_status === 'completed');
      } else if (chapterFilter.value === 'pending') {
        list = list.filter(c => c.translation_status !== 'completed');
      }

      if (chapterSearch.value.trim()) {
        const q = chapterSearch.value.toLowerCase();
        list = list.filter(c =>
          c.title.toLowerCase().includes(q) ||
          (c.title_translated && c.title_translated.toLowerCase().includes(q)) ||
          c.chapter_index.toString() === q
        );
      }
      return list;
    });

    // Bilingual paragraph pairing
    const pairedParagraphs = computed(() => {
      if (!currentChapter.value) return [];
      const transText = streamingText.value || currentChapter.value.translated_content || '';
      const viParagraphs = transText ? transText.split(/\n\s*\n/).map(p => p.trim()).filter(Boolean) : [];
      const zhParagraphs = currentChapter.value.raw_content ? currentChapter.value.raw_content.split(/\n\s*\n/).map(p => p.trim()).filter(Boolean) : [];

      const maxLen = Math.max(viParagraphs.length, zhParagraphs.length);
      const pairs = [];
      for (let i = 0; i < maxLen; i++) {
        pairs.push({
          vi: viParagraphs[i] || '',
          zh: zhParagraphs[i] || ''
        });
      }
      return pairs;
    });

    // 15. Discover Online Novels
    async function loadDiscoverCategories() {
      try {
        const res = await fetch('/api/discover/categories');
        discoverCategories.value = await res.json();
      } catch (e) {
        console.warn('Lỗi tải categories:', e);
      }
    }

    async function loadDiscoverNovels(resetPage = true) {
      if (resetPage) {
        discoverPage.value = 1;
        isDiscoverLoading.value = true;
      }
      try {
        let url = `/api/discover/novels?category=${selectedDiscoverCategory.value}&sort_by=${discoverSort.value}&time_range=${discoverTimeRange.value}&source_mode=${selectedSourceMode.value}&page=${discoverPage.value}&page_size=24`;
        if (discoverSearch.value.trim()) {
          url += `&search=${encodeURIComponent(discoverSearch.value.trim())}`;
        }
        const res = await fetch(url);
        const data = await res.json();
        if (Array.isArray(data)) {
          discoverNovels.value = data;
          discoverTotal.value = data.length;
          discoverHasMore.value = false;
        } else if (data && data.items) {
          if (resetPage) {
            discoverNovels.value = data.items;
          } else {
            discoverNovels.value.push(...data.items);
          }
          discoverTotal.value = data.total;
          discoverHasMore.value = data.has_more;
        }
      } catch (e) {
        showToast('Lỗi khi tải danh sách khám phá', 'error');
      } finally {
        isDiscoverLoading.value = false;
        isDiscoverLoadingMore.value = false;
      }
    }

    async function loadMoreDiscoverNovels() {
      if (isDiscoverLoadingMore.value || !discoverHasMore.value) return;
      discoverPage.value++;
      isDiscoverLoadingMore.value = true;
      await loadDiscoverNovels(false);
    }

    async function cloneAndReadNovel(catalogItem, openImmediately = false) {
      if (cloningNovelId.value) return;
      cloningNovelId.value = catalogItem.id;
      showToast(`Đang tải truyện '${catalogItem.title_vi}' về máy & chuẩn bị dịch...`, 'info', 3000);

      try {
        const res = await fetch('/api/discover/clone', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            catalog_id: catalogItem.id,
            auto_translate_first: 3,
            source_url: catalogItem.source_url,
            title: catalogItem.title,
            title_vi: catalogItem.title_vi,
            author: catalogItem.author,
            cover_url: catalogItem.cover_url,
            category: catalogItem.category
          })
        });
        if (!res.ok) {
          const err = await res.json();
          throw new Error(err.detail || 'Lỗi khi tải truyện');
        }
        const result = await res.json();
        showToast(result.message || 'Đã clone truyện về máy thành công!', 'success', 4000);

        catalogItem.is_downloaded = true;
        catalogItem.local_novel_id = result.novel_id;

        await loadNovels();

        if (openImmediately && result.first_chapter_id) {
          await openChapter(result.first_chapter_id);
        } else if (result.novel_id) {
          await openNovelDetail(result.novel_id);
        }
      } catch (err) {
        showToast(err.message, 'error');
      } finally {
        cloningNovelId.value = null;
      }
    }

    // --- Fullscreen & View Helpers ---
    function toggleFullscreen() {
      if (!document.fullscreenElement && !document.webkitFullscreenElement) {
        const docEl = document.documentElement;
        if (docEl.requestFullscreen) {
          docEl.requestFullscreen().catch(e => console.warn(e));
        } else if (docEl.webkitRequestFullscreen) {
          docEl.webkitRequestFullscreen();
        }
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen().catch(e => console.warn(e));
        } else if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        }
      }
    }

    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function toggleFullWidth() {
      readerSettings.maxWidth = '100%';
      localStorage.setItem('reader_max_width', '100%');
      if (readerSettings.sidePadding === 'compact') {
        updateReaderSetting('sidePadding', 'tight');
        showToast('Toàn trang 100% - Lề mỏng sát viền (12px)', 'success', 2500);
      } else if (readerSettings.sidePadding === 'tight') {
        updateReaderSetting('sidePadding', 'normal');
        showToast('Toàn trang 100% - Lề thoáng (48px)', 'info', 2500);
      } else {
        updateReaderSetting('sidePadding', 'compact');
        showToast('Toàn trang 100% - Lề tiêu chuẩn (24px)', 'success', 2500);
      }
    }

    // --- Keyboard & Touch Listeners for Reader ---
    function handleKeydown(e) {
      if (currentView.value !== 'reader' || !currentChapter.value) return;
      if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

      if ((e.key === 'ArrowRight' || e.key === 'd' || e.key === 'D') && currentChapter.value.next_id) {
        openChapter(currentChapter.value.next_id);
      } else if ((e.key === 'ArrowLeft' || e.key === 'a' || e.key === 'A') && currentChapter.value.prev_id) {
        openChapter(currentChapter.value.prev_id);
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      } else if (e.key === 'w' || e.key === 'W') {
        toggleFullWidth();
      } else if (e.key === 'm' || e.key === 'M') {
        showTocDrawer.value = !showTocDrawer.value;
      } else if (e.key === 't' || e.key === 'T') {
        scrollToTop();
      }
    }

    // Scroll listener for reading progress & floating bar hide/show
    function handleScroll() {
      if (currentView.value !== 'reader' || !currentChapter.value) return;
      const scrollY = window.scrollY;
      const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (scrollHeight > 0) {
        const progress = Math.min(100, Math.max(0, (scrollY / scrollHeight) * 100));
        readingProgress.value = Math.round(progress);
        syncReadingProgress(currentChapter.value.novel_id, currentChapter.value.id, currentChapter.value.chapter_index, progress);
      }

      // Auto-hide controls when scrolling down fast, show when scrolling up
      if (scrollY > lastScrollY && scrollY > 150) {
        showReaderControls.value = false;
      } else if (scrollY < lastScrollY - 20) {
        showReaderControls.value = true;
      }
      lastScrollY = scrollY;
    }

    function handleFsChange() {
      isFullscreen.value = !!(document.fullscreenElement || document.webkitFullscreenElement);
    }

    const checkAuthStatus = async () => {
      try {
        const res = await _originalFetch('/api/auth/status');
        const data = await res.json();
        authRequiresPasscode.value = data.requires_passcode;
        isEnvLocked.value = data.is_env_locked;
        
        if (data.requires_passcode) {
          const savedPasscode = localStorage.getItem('novel_app_passcode') || sessionStorage.getItem('novel_app_passcode');
          if (savedPasscode) {
            const verifyRes = await _originalFetch('/api/auth/verify', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ passcode: savedPasscode })
            });
            if (verifyRes.ok) {
              isAppLocked.value = false;
              return true;
            }
          }
          isAppLocked.value = true;
          return false;
        } else {
          isAppLocked.value = false;
          return true;
        }
      } catch (err) {
        console.error('Lỗi kiểm tra xác thực:', err);
        return false;
      } finally {
        isAuthChecking.value = false;
      }
    };

    const unlockApp = async () => {
      if (!inputPasscode.value) {
        authError.value = 'Vui lòng nhập mật khẩu mở khóa';
        return;
      }
      authError.value = '';
      try {
        const res = await _originalFetch('/api/auth/verify', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ passcode: inputPasscode.value })
        });
        if (res.ok) {
          if (rememberDevice.value) {
            localStorage.setItem('novel_app_passcode', inputPasscode.value);
          } else {
            sessionStorage.setItem('novel_app_passcode', inputPasscode.value);
          }
          isAppLocked.value = false;
          authError.value = '';
          inputPasscode.value = '';
          showToast('Đã mở khóa thành công!', 'success');
          await loadNovels();
          await loadDiscoverCategories();
          await loadDiscoverNovels();
        } else {
          authError.value = 'Mật khẩu không chính xác. Vui lòng thử lại!';
        }
      } catch (err) {
        authError.value = 'Lỗi kết nối máy chủ: ' + err.message;
      }
    };

    const savePasscodeSetting = async () => {
      try {
        const res = await fetch('/api/auth/set-passcode', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            old_passcode: oldPasscode.value,
            new_passcode: newPasscode.value
          })
        });
        const data = await res.json();
        if (res.ok) {
          if (newPasscode.value) {
            localStorage.setItem('novel_app_passcode', newPasscode.value);
            authRequiresPasscode.value = true;
          } else {
            localStorage.removeItem('novel_app_passcode');
            sessionStorage.removeItem('novel_app_passcode');
            authRequiresPasscode.value = false;
          }
          newPasscode.value = '';
          oldPasscode.value = '';
          showToast(data.message || 'Đã lưu cấu hình mật khẩu!', 'success');
        } else {
          showToast(data.detail || 'Không thể lưu mật khẩu', 'error');
        }
      } catch (err) {
        showToast('Lỗi: ' + err.message, 'error');
      }
    };

    const lockAppNow = () => {
      localStorage.removeItem('novel_app_passcode');
      sessionStorage.removeItem('novel_app_passcode');
      isAppLocked.value = true;
      showToast('Đã khóa ứng dụng!', 'info');
    };

    onMounted(async () => {
      window.addEventListener('novel-auth-required', () => {
        isAppLocked.value = true;
      });

      const isAllowed = await checkAuthStatus();
      if (isAllowed) {
        await loadNovels();
        await loadDiscoverCategories();
        await loadDiscoverNovels();
        await loadSettings();
        await loadScraperRules();
      }

      window.addEventListener('keydown', handleKeydown);
      window.addEventListener('scroll', handleScroll, { passive: true });
      document.addEventListener('fullscreenchange', handleFsChange);
      document.addEventListener('webkitfullscreenchange', handleFsChange);

      // Service Worker registration
      if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js').then(reg => {
          reg.update();
        }).catch(err => {
          console.warn('SW registration failed:', err);
        });
      }
    });

    onUnmounted(() => {
      window.removeEventListener('keydown', handleKeydown);
      window.removeEventListener('scroll', handleScroll);
      document.removeEventListener('fullscreenchange', handleFsChange);
      document.removeEventListener('webkitfullscreenchange', handleFsChange);
    });

    return {
      isAppLocked,
      isAuthChecking,
      authRequiresPasscode,
      isEnvLocked,
      inputPasscode,
      rememberDevice,
      authError,
      newPasscode,
      oldPasscode,
      unlockApp,
      savePasscodeSetting,
      lockAppNow,
      activeMainTab,
      discoverCategories,
      selectedDiscoverCategory,
      selectedSourceMode,
      discoverSort,
      discoverTimeRange,
      discoverSearch,
      discoverNovels,
      discoverPage,
      discoverTotal,
      discoverHasMore,
      isDiscoverLoading,
      isDiscoverLoadingMore,
      cloningNovelId,
      previewNovel,
      showPreviewModal,
      openNovelPreview,
      closeNovelPreview,
      loadDiscoverCategories,
      loadDiscoverNovels,
      loadMoreDiscoverNovels,
      cloneAndReadNovel,
      currentView,
      selectedNovelId,
      selectedNovel,
      currentChapter,
      novels,
      chapters,
      filteredNovels,
      filteredChapters,
      chapterSearch,
      chapterFilter,
      librarySearch,
      isLoading,
      isTranslating,
      streamingText,
      toast,
      showAddModal,
      addTab,
      showBatchModal,
      showSettingsModal,
      showTocDrawer,
      showGlossaryExtractModal,
      showAddGlossaryModal,
      showEditRuleModal,
      showReaderControls,
      isBilingual,
      isShowingRawFallback,
      isFullscreen,
      readingProgress,
      isChapterAnimate,
      toggleFullscreen,
      toggleFullWidth,
      scrollToTop,
      requestAntigravityTranslation,
      readerSettings,
      novelUrlForm,
      novelRawForm,
      batchForm,
      showBulkDownloadModal,
      bulkDownloadLoading,
      bulkDownloadForm,
      scrapeStatus,
      loadScrapeStatus,
      openBulkDownloadModal,
      submitBulkDownload,
      exportNovelTxt,
      aiSettings,
      availableModels,
      isTestingAi,
      aiTestResult,
      glossaryItems,
      glossaryCategory,
      glossarySearch,
      glossaryForm,
      glossarySuggestions,
      selectedSuggestions,
      isExtractingGlossary,
      scraperRules,
      currentRule,
      pairedParagraphs,
      showToast,
      updateReaderSetting,
      loadNovels,
      openNovelDetail,
      submitNovelUrl,
      submitNovelRaw,
      handleFileUpload,
      deleteNovel,
      openChapter,
      startStreamTranslation,
      submitBatchTranslate,
      triggerExtractGlossary,
      applySelectedGlossarySuggestions,
      loadGlossary,
      saveGlossaryItem,
      deleteGlossaryItem,
      openEditGlossary,
      saveSettings,
      fetchAiModels,
      testAiConnection,
      saveRule,
      deleteRule,
      openEditRule
    };
  }
});

app.mount('#app');

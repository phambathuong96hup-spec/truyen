import re
import urllib.parse
from typing import Dict, Any, List, Optional, Tuple
import httpx
from bs4 import BeautifulSoup
import charset_normalizer

try:
    import cloudscraper
    HAS_CLOUDSCRAPER = True
except ImportError:
    HAS_CLOUDSCRAPER = False

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
]

DEFAULT_SCRAPER_RULES = [
    {
        "domain": "69shuba.cx",
        "name": "69 Thư Ba (.cx)",
        "novel_title_selector": "h1, .booknav2 h1, .bookinfo h1",
        "novel_author_selector": ".booknav2 p:nth-of-type(1) a, .bookinfo p a",
        "novel_cover_selector": ".bookimg2 img, .bookinfo img",
        "novel_desc_selector": ".navtxt, .intro",
        "chapter_list_selector": "#catalog ul, .catalog ul, #chaperlist",
        "chapter_link_selector": "li a",
        "chapter_title_selector": "h1, .hide-title, .txtnav h1",
        "chapter_content_selector": ".txtnav, #content",
        "content_remove_selectors": "script,style,div.bottom-ad,div.ad,ins,.ad",
        "encoding": "gb18030"
    },
    {
        "domain": "69shuba.com",
        "name": "69 Thư Ba (.com)",
        "novel_title_selector": "h1, .booknav2 h1, .bookinfo h1",
        "novel_author_selector": ".booknav2 p:nth-of-type(1) a, .bookinfo p a",
        "novel_cover_selector": ".bookimg2 img, .bookinfo img",
        "novel_desc_selector": ".navtxt, .intro",
        "chapter_list_selector": "#catalog ul, .catalog ul, #chaperlist",
        "chapter_link_selector": "li a",
        "chapter_title_selector": "h1, .txtnav h1",
        "chapter_content_selector": ".txtnav, #content",
        "content_remove_selectors": "script,style,div.bottom-ad,div.ad,ins,.ad",
        "encoding": "gb18030"
    },
    {
        "domain": "biquge.tv",
        "name": "Bút Thú Các (biquge.tv)",
        "novel_title_selector": "#info h1, .info h1",
        "novel_author_selector": "#info p:nth-of-type(1), .info p a",
        "novel_cover_selector": "#fmimg img",
        "novel_desc_selector": "#intro",
        "chapter_list_selector": "#list dl, .listmain dl",
        "chapter_link_selector": "dd a",
        "chapter_title_selector": ".bookname h1, h1",
        "chapter_content_selector": "#content",
        "content_remove_selectors": "script,style,p.readinline",
        "encoding": "utf-8"
    },
    {
        "domain": "uukanshu.com",
        "name": "UU Độc Thư (uukanshu.com)",
        "novel_title_selector": "h1.booktitle, .book-info h1",
        "novel_author_selector": "h2.bookauthor, .book-info h2",
        "novel_cover_selector": ".book-img img",
        "novel_desc_selector": ".book-intro, #bookintro",
        "chapter_list_selector": "#chapterList",
        "chapter_link_selector": "li a",
        "chapter_title_selector": "h1#timu, h1",
        "chapter_content_selector": "#contentbox, .contentbox",
        "content_remove_selectors": "script,style,.ad_content",
        "encoding": "gb18030"
    },
    {
        "domain": "piaotia.com",
        "name": "Phiêu Thiên Văn Học (piaotia.com)",
        "novel_title_selector": "h1, caption h1",
        "novel_author_selector": "td:contains('作 者')",
        "novel_cover_selector": "img.pic",
        "novel_desc_selector": "span.hottext",
        "chapter_list_selector": ".centent, td.mainbdy",
        "chapter_link_selector": "li a, td a",
        "chapter_title_selector": "h1",
        "chapter_content_selector": "#content",
        "content_remove_selectors": "script,style,div[align='center']",
        "encoding": "gbk"
    }
]

def extract_domain(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    domain = parsed.netloc.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return domain

def detect_and_decode(content_bytes: bytes, explicit_encoding: Optional[str] = None) -> str:
    """Smart encoding detector for Chinese webpages (GBK/GB18030/UTF-8/Big5)"""
    if explicit_encoding and explicit_encoding != "auto":
        try:
            return content_bytes.decode(explicit_encoding, errors="replace")
        except Exception:
            pass

    # 1. Check meta tag in head
    head_peek = content_bytes[:2048]
    meta_charset = re.search(rb'charset=["\']?([\w-]+)', head_peek, re.IGNORECASE)
    if meta_charset:
        enc_name = meta_charset.group(1).decode("ascii", errors="ignore").lower()
        if "gb" in enc_name:
            enc_name = "gb18030"  # gb18030 is full superset of gbk and gb2312
        try:
            return content_bytes.decode(enc_name, errors="replace")
        except Exception:
            pass

    # 2. Try UTF-8 directly
    try:
        return content_bytes.decode("utf-8")
    except UnicodeDecodeError:
        pass

    # 3. Try GB18030 (standard for Chinese sites)
    try:
        return content_bytes.decode("gb18030")
    except UnicodeDecodeError:
        pass

    # 4. Use charset_normalizer
    res = charset_normalizer.detect(content_bytes)
    if res and res.get("encoding"):
        try:
            return content_bytes.decode(res["encoding"], errors="replace")
        except Exception:
            pass

    # Final fallback
    return content_bytes.decode("utf-8", errors="replace")

async def fetch_page_content(url: str, encoding: Optional[str] = None) -> Tuple[str, str]:
    """Fetch URL and return (html_string, final_url) with anti-bot fallback"""
    headers = {
        "User-Agent": USER_AGENTS[0],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": url,
        "Cache-Control": "no-cache",
    }

    try:
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=25.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                html = detect_and_decode(resp.content, explicit_encoding=encoding)
                return html, str(resp.url)
    except Exception as e:
        # Fallback to cloudscraper if available
        if HAS_CLOUDSCRAPER:
            scraper = cloudscraper.create_scraper()
            resp = scraper.get(url, headers=headers, timeout=25)
            if resp.status_code == 200:
                html = detect_and_decode(resp.content, explicit_encoding=encoding)
                return html, str(resp.url)
        raise e

    # If status code not 200, try cloudscraper
    if HAS_CLOUDSCRAPER:
        scraper = cloudscraper.create_scraper()
        resp = scraper.get(url, headers=headers, timeout=25)
        if resp.status_code == 200:
            html = detect_and_decode(resp.content, explicit_encoding=encoding)
            return html, str(resp.url)

    raise ValueError(f"Không thể tải trang: HTTP {resp.status_code if 'resp' in locals() else 'Connection failed'}")

def clean_extracted_text(text: str) -> str:
    """Normalize whitespace and paragraphs for novel reading"""
    lines = [line.strip() for line in text.splitlines()]
    cleaned_lines = []
    for line in lines:
        if not line:
            continue
        # Remove watermarks / ads patterns in Chinese novels
        if any(ad in line for ad in [
            "69书吧", "69shuba", "笔趣阁", "uukanshu", "一秒记住", "手机版阅读网址", 
            "本章未完，点击下一页", "无弹窗", "投推荐票", "加入书签"
        ]):
            continue
        cleaned_lines.append(line)
    return "\n\n".join(cleaned_lines)

def auto_detect_content(soup: BeautifulSoup) -> Tuple[str, str]:
    """Smart heuristic algorithm to extract chapter title and body from unknown HTML"""
    # 1. Extract title
    title = ""
    for sel in ["h1", ".title", ".chapter-title", "header h1", "h2"]:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 2:
            title = el.get_text(strip=True)
            break
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            t = title_tag.get_text(strip=True)
            title = t.split("_")[0].split("-")[0].strip()

    # 2. Remove script, style, ads
    for tag in soup(["script", "style", "noscript", "iframe", "header", "footer", "nav", "aside", "svg"]):
        tag.decompose()

    # 3. Find candidate content containers
    candidates = soup.select("#content, .content, #chaptercontent, .txtnav, .read-content, #booktxt, #htmlContent, article, .text")
    best_text = ""
    if candidates:
        for c in candidates:
            # Replace <br> and <p> with newlines
            for br in c.find_all(["br", "p"]):
                br.replace_with(f"\n{br.get_text()}\n")
            txt = c.get_text()
            if len(txt) > len(best_text):
                best_text = txt

    # 4. If still not found, search all divs for largest Chinese text density
    if len(best_text.strip()) < 100:
        divs = soup.find_all("div")
        for d in divs:
            for br in d.find_all(["br", "p"]):
                br.replace_with(f"\n{br.get_text()}\n")
            txt = d.get_text()
            # Count Chinese characters
            c_count = len(re.findall(r'[\u4e00-\u9fff]', txt))
            if c_count > 200 and len(txt) > len(best_text):
                best_text = txt

    # 5. Fallback for sites where text is directly under body (like piaotia)
    if len(best_text.strip()) < 100 and soup.body:
        for tag in soup.body.find_all(["table", "ul", "ol", "form", "center"]):
            tag.decompose()
        for br in soup.body.find_all(["br", "p"]):
            br.replace_with(f"\n{br.get_text()}\n")
        body_txt = soup.body.get_text()
        c_count = len(re.findall(r'[\u4e00-\u9fff]', body_txt))
        if c_count > 150 and len(body_txt) > len(best_text):
            best_text = body_txt

    cleaned = clean_extracted_text(best_text)
    return title or "Chương không tiêu đề", cleaned

def auto_detect_novel_info(soup: BeautifulSoup, page_url: str) -> Dict[str, Any]:
    """Heuristic info extractor for novel detail page"""
    title = ""
    author = "Chưa rõ"
    cover_url = ""
    desc = ""

    # OpenGraph meta tags
    og_title = soup.find("meta", property="og:novel:book_name") or soup.find("meta", property="og:title")
    if og_title and og_title.get("content"):
        title = og_title["content"].strip()

    og_author = soup.find("meta", property="og:novel:author")
    if og_author and og_author.get("content"):
        author = og_author["content"].strip()

    og_cover = soup.find("meta", property="og:image")
    if og_cover and og_cover.get("content"):
        cover_url = urllib.parse.urljoin(page_url, og_cover["content"].strip())

    og_desc = soup.find("meta", property="og:description")
    if og_desc and og_desc.get("content"):
        desc = og_desc["content"].strip()

    # DOM Fallbacks
    if not title:
        t_el = soup.select_one("h1, .book-name, .bookinfo h1, .info h1")
        if t_el:
            title = t_el.get_text(strip=True)

    if author == "Chưa rõ":
        # Search text like "作者：xxx"
        text_match = re.search(r'作者[：:]\s*([^\s<"\'&]+)', soup.get_text())
        if text_match:
            author = text_match.group(1).strip()
        else:
            a_el = soup.select_one(".author, a[href*='author'], .bookinfo p a")
            if a_el:
                author = a_el.get_text(strip=True)

    if not cover_url:
        img = soup.select_one(".bookimg img, .cover img, .pic img, #fmimg img, .book-img img")
        if img:
            src = img.get("src") or img.get("data-src") or ""
            if src:
                cover_url = urllib.parse.urljoin(page_url, src)

    if not desc:
        desc_el = soup.select_one("#intro, .intro, .book-intro, .navtxt, .description")
        if desc_el:
            desc = desc_el.get_text(strip=True)

    return {
        "title": title or "Tiểu thuyết chưa đặt tên",
        "author": author or "Chưa rõ",
        "cover_url": cover_url,
        "description": desc or "Chưa có mô tả.",
    }

def extract_chapter_links(soup: BeautifulSoup, page_url: str, custom_rule: Optional[Dict[str, Any]] = None) -> List[Dict[str, str]]:
    """Extract table of contents links from novel catalog page"""
    chapters = []
    seen_urls = set()

    # 1. Custom rule if provided
    if custom_rule and custom_rule.get("chapter_list_selector"):
        container = soup.select_one(custom_rule["chapter_list_selector"])
        link_selector = custom_rule.get("chapter_link_selector") or "a"
        if container:
            links = container.select(link_selector)
        else:
            links = soup.select(link_selector)
    else:
        # Heuristic: search container with id/class matching catalog keywords
        containers = soup.select("#catalog, #chapterList, #list, .catalog, .chapter-list, .section-box, .mulu, .listmain, #chaperlist")
        if containers:
            links = containers[0].find_all("a")
        else:
            links = soup.find_all("a")

    for a in links:
        href = a.get("href")
        if not href or href.startswith("javascript:") or href.startswith("#"):
            continue

        raw_title = a.get_text(strip=True)
        # Check if text looks like a chapter title (e.g. 第...章 or contains numbers/title keywords)
        if len(raw_title) < 2:
            continue

        abs_url = urllib.parse.urljoin(page_url, href)
        if abs_url in seen_urls:
            continue

        # Filter out common non-chapter links like homepage, book info, category links
        if abs_url.rstrip("/") == page_url.rstrip("/"):
            continue

        seen_urls.add(abs_url)
        chapters.append({
            "title": raw_title,
            "url": abs_url
        })

    # Filter out "Latest Chapters Preview" prefix that some Chinese sites (Biquge/8tsw/etc.) put before Chapter 1
    for idx, ch in enumerate(chapters):
        if 0 < idx < 30 and re.search(r'第[1一01]章|^[1一01][\s、\.\:]', ch['title']):
            chapters = chapters[idx:]
            break

    return chapters

async def scrape_novel_info_and_chapters(url: str, rule: Optional[Dict[str, Any]] = None, auto_detect: bool = True) -> Dict[str, Any]:
    """Top-level scraper function for novel catalog page"""
    encoding = rule.get("encoding") if rule else None
    html, final_url = await fetch_page_content(url, encoding=encoding)
    soup = BeautifulSoup(html, "lxml")

    # Novel info
    if rule and not auto_detect:
        title_el = soup.select_one(rule.get("novel_title_selector", "h1"))
        author_el = soup.select_one(rule.get("novel_author_selector", ""))
        cover_el = soup.select_one(rule.get("novel_cover_selector", ""))
        desc_el = soup.select_one(rule.get("novel_desc_selector", ""))

        title = title_el.get_text(strip=True) if title_el else "Tiểu thuyết"
        author = author_el.get_text(strip=True) if author_el else "Chưa rõ"
        cover_url = ""
        if cover_el:
            cover_url = urllib.parse.urljoin(final_url, cover_el.get("src") or cover_el.get("data-src") or "")
        desc = desc_el.get_text(strip=True) if desc_el else ""

        info = {
            "title": title,
            "author": author,
            "cover_url": cover_url,
            "description": desc,
        }
    else:
        info = auto_detect_novel_info(soup, final_url)

    # Chapters list
    chapters = extract_chapter_links(soup, final_url, custom_rule=rule)

    return {
        "info": info,
        "chapters": chapters,
        "source_url": final_url
    }

async def scrape_single_chapter(url: str, rule: Optional[Dict[str, Any]] = None) -> Dict[str, str]:
    """Fetch and parse content of a single chapter"""
    encoding = rule.get("encoding") if rule else None
    html, final_url = await fetch_page_content(url, encoding=encoding)
    soup = BeautifulSoup(html, "lxml")

    if rule and rule.get("chapter_content_selector"):
        # Remove unwanted items
        if rule.get("content_remove_selectors"):
            for sel in rule["content_remove_selectors"].split(","):
                sel = sel.strip()
                if sel:
                    for rm in soup.select(sel):
                        rm.decompose()

        # Title
        title = "Chương"
        if rule.get("chapter_title_selector"):
            t_el = soup.select_one(rule["chapter_title_selector"])
            if t_el:
                title = t_el.get_text(strip=True)

        # Content
        content_el = soup.select_one(rule["chapter_content_selector"])
        if content_el:
            for br in content_el.find_all(["br", "p"]):
                br.replace_with(f"\n{br.get_text()}\n")
            raw_content = clean_extracted_text(content_el.get_text())
        else:
            title, raw_content = auto_detect_content(soup)
    else:
        title, raw_content = auto_detect_content(soup)

    return {
        "title": title,
        "raw_content": raw_content,
        "source_url": final_url
    }

def parse_raw_text_into_chapters(raw_text: str) -> List[Dict[str, str]]:
    """Parse pasted Chinese novel text or uploaded .txt file into chapter objects"""
    # Regex matching chapter headings: 第...章 or 第...回 or 第...节 or Chapter ...
    pattern = re.compile(
        r'(?:^|\n)\s*(第\s*[\d一二三四五六七八九十百千万0-9]+\s*[章回节卷部集][^\n]*)',
        re.MULTILINE
    )

    matches = list(pattern.finditer(raw_text))
    if not matches:
        # Fallback: Treat as 1 chapter or split by 3000 chars
        return [{
            "title": "Chương 1",
            "raw_content": clean_extracted_text(raw_text)
        }]

    chapters = []
    for i, match in enumerate(matches):
        ch_title = match.group(1).strip()
        start_pos = match.end()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(raw_text)
        ch_content = raw_text[start_pos:end_pos].strip()

        chapters.append({
            "title": ch_title,
            "raw_content": clean_extracted_text(ch_content)
        })

    return chapters

import asyncio
import json
import logging
from typing import List, Dict, Any, Optional, AsyncGenerator
import httpx
from sqlalchemy import select, update
from backend.config import (
    DEFAULT_API_BASE_URL,
    DEFAULT_API_KEY,
    DEFAULT_MODEL_NAME,
    DEFAULT_TEMPERATURE,
    DEFAULT_SYSTEM_PROMPT
)
from backend.database import AsyncSessionLocal
from backend.models import Chapter, Glossary, AppSetting, Novel, TranslationTask

logger = logging.getLogger("translator")

class TranslationService:
    def __init__(self):
        self.queue: asyncio.Queue = asyncio.Queue()
        self.active_tasks: set = set()
        self._worker_task: Optional[asyncio.Task] = None
        self._is_running = False

    def start_background_worker(self):
        if not self._is_running:
            self._is_running = True
            self._worker_task = asyncio.create_task(self._process_queue())
            logger.info("Background translation worker started.")

    async def stop_background_worker(self):
        self._is_running = False
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass

    async def get_ai_settings(self) -> Dict[str, Any]:
        """Fetch saved AI settings from SQLite or fallback to defaults"""
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(AppSetting))
            settings = {s.key: s.value for s in result.scalars().all()}

        return {
            "api_base_url": settings.get("ai_base_url") or DEFAULT_API_BASE_URL,
            "api_key": settings.get("ai_api_key") or DEFAULT_API_KEY,
            "model_name": settings.get("ai_model_name") or DEFAULT_MODEL_NAME,
            "temperature": float(settings.get("ai_temperature") or DEFAULT_TEMPERATURE),
            "system_prompt": settings.get("ai_system_prompt") or DEFAULT_SYSTEM_PROMPT,
        }

    async def save_ai_settings(self, settings: Dict[str, Any]):
        async with AsyncSessionLocal() as session:
            for k, v in settings.items():
                setting_key = f"ai_{k}" if not k.startswith("ai_") else k
                db_setting = await session.get(AppSetting, setting_key)
                if db_setting:
                    db_setting.value = str(v)
                else:
                    session.add(AppSetting(key=setting_key, value=str(v)))
            await session.commit()

    async def fetch_available_models(self, api_base_url: Optional[str] = None, api_key: Optional[str] = None) -> List[str]:
        """Fetch list of available models from OpenAI-compatible endpoint (Ollama, LM Studio, etc.)"""
        settings = await self.get_ai_settings()
        base_url = (api_base_url or settings["api_base_url"]).rstrip("/")
        key = api_key if api_key is not None else settings["api_key"]

        headers = {}
        if key:
            headers["Authorization"] = f"Bearer {key}"

        url = f"{base_url}/models"
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                if "data" in data and isinstance(data["data"], list):
                    return [item["id"] for item in data["data"] if "id" in item]
                elif isinstance(data, list):
                    return [item["id"] for item in data if "id" in item]
            raise ValueError(f"HTTP {resp.status_code}: {resp.text}")

    def build_glossary_prompt(self, raw_text: str, glossary_items: List[Glossary]) -> str:
        """Filter glossary terms present in raw text and format into prompt injection"""
        matched_terms = []
        for item in glossary_items:
            if item.source_term in raw_text:
                cat_label = {
                    "nhan_vat": "Nhân vật",
                    "canh_gioi": "Cảnh giới",
                    "dia_danh": "Địa danh",
                    "cong_phap": "Công pháp/Chiêu thức",
                    "vat_pham": "Pháp bảo/Vật phẩm",
                    "khac": "Khác"
                }.get(item.category, "Thuật ngữ")
                matched_terms.append(f"- [{cat_label}] {item.source_term} -> {item.target_term}")

        if not matched_terms:
            return ""

        return (
            "\n\nBẢNG TỪ ĐIỂN TÊN RIÊNG & THUẬT NGỮ BẮT BUỘC TUÂN THỦ (GLOSSARY):\n"
            + "\n".join(matched_terms)
            + "\n(Lưu ý: Bắt buộc dịch đúng 100% theo các cặp từ trên khi xuất hiện trong văn bản!)\n"
        )

    async def translate_chapter(self, chapter_id: int, force: bool = False) -> str:
        """Translate a single chapter completely and save to DB"""
        async with AsyncSessionLocal() as session:
            chapter = await session.get(Chapter, chapter_id)
            if not chapter:
                raise ValueError("Chapter not found")

            if chapter.translation_status == "completed" and chapter.translated_content and not force:
                return chapter.translated_content

            # Mark as translating
            chapter.translation_status = "translating"
            chapter.error_message = None
            await session.commit()

            # Load glossary for this novel
            gloss_result = await session.execute(
                select(Glossary).where(Glossary.novel_id == chapter.novel_id)
            )
            glossary_items = gloss_result.scalars().all()

        settings = await self.get_ai_settings()

        # If no cloud API key is configured or base_url is localhost:
        # DO NOT call localhost or Ollama! Queue for Antigravity instead.
        if not settings.get("api_key") or "localhost" in settings.get("api_base_url", ""):
            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    novel = await session.get(Novel, ch.novel_id)
                    novel_title = novel.title if novel else ""
                    task = TranslationTask(
                        novel_id=ch.novel_id,
                        novel_title=novel_title,
                        chapter_index=ch.chapter_index,
                        chapter_count=1,
                        status="pending",
                        notes=f"Yêu cầu từ Reader trực tiếp (Chương {ch.chapter_index})"
                    )
                    session.add(task)
                    ch.translation_status = "pending"
                    ch.error_message = None
                    await session.commit()
            
            logger.info(f"Chapter {chapter_id} safely queued for Antigravity (no external cloud key).")
            return ""

        glossary_prompt = self.build_glossary_prompt(
            f"{chapter.title}\n{chapter.raw_content}", glossary_items
        )

        user_content = (
            f"Hãy dịch tiêu đề và toàn bộ nội dung chương sau đây sang tiếng Việt tiểu thuyết mượt mà, giữ tương ứng đoạn văn:\n\n"
            f"[TIÊU ĐỀ GỐC]: {chapter.title}\n\n"
            f"[NỘI DUNG GỐC]:\n{chapter.raw_content}"
            f"{glossary_prompt}"
        )

        headers = {"Content-Type": "application/json"}
        if settings["api_key"]:
            headers["Authorization"] = f"Bearer {settings['api_key']}"

        payload = {
            "model": settings["model_name"],
            "messages": [
                {"role": "system", "content": settings["system_prompt"]},
                {"role": "user", "content": user_content}
            ],
            "temperature": settings["temperature"],
            "stream": False
        }

        base_url = settings["api_base_url"].rstrip("/")
        url = f"{base_url}/chat/completions"

        try:
            async with httpx.AsyncClient(timeout=180.0) as client:
                resp = await client.post(url, json=payload, headers=headers)
                if resp.status_code != 200:
                    raise ValueError(f"AI API returned error: {resp.status_code} - {resp.text}")

                res_json = resp.json()
                translated_text = res_json["choices"][0]["message"]["content"].strip()

            # Extract translated title if present in first line
            lines = [line.strip() for line in translated_text.splitlines() if line.strip()]
            translated_title = lines[0] if lines else chapter.title
            # Clean title tags like "[TIÊU ĐỀ]: " if model returned it
            translated_title = translated_title.replace("[TIÊU ĐỀ DỊCH]:", "").replace("[TIÊU ĐỀ]:", "").strip()

            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    ch.translated_content = translated_text
                    ch.title_translated = translated_title
                    ch.translation_status = "completed"
                    ch.error_message = None
                    await session.commit()

            return translated_text

        except Exception as e:
            err_msg = str(e)
            if "All connection attempts failed" in err_msg or "Connect call failed" in err_msg or "WinError 10061" in err_msg:
                err_msg = (
                    "Không thể kết nối đến máy chủ AI API đã cấu hình. "
                    "Vui lòng kiểm tra lại đường dẫn API Base URL và API Key trong mục Cài đặt (⚙️), "
                    "hoặc yêu cầu Antigravity dịch trực tiếp bằng Gemini 3.8 Flash."
                )
            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    ch.translation_status = "failed"
                    ch.error_message = err_msg
                    await session.commit()
            raise ValueError(err_msg)

    async def stream_translate_chapter(self, chapter_id: int, force: bool = False) -> AsyncGenerator[str, None]:
        """Stream translation chunks via SSE and persist full result to DB upon completion"""
        async with AsyncSessionLocal() as session:
            chapter = await session.get(Chapter, chapter_id)
            if not chapter:
                yield f"data: {json.dumps({'error': 'Chapter not found'})}\n\n"
                return

            if chapter.translation_status == "completed" and chapter.translated_content and not force:
                # Already translated, yield cached
                yield f"data: {json.dumps({'chunk': chapter.translated_content, 'done': True, 'title_translated': chapter.title_translated})}\n\n"
                return

            chapter.translation_status = "translating"
            await session.commit()

            gloss_result = await session.execute(
                select(Glossary).where(Glossary.novel_id == chapter.novel_id)
            )
            glossary_items = gloss_result.scalars().all()

        settings = await self.get_ai_settings()

        # If no cloud API key is configured or base_url is localhost:
        # DO NOT call localhost or Ollama! Queue for Antigravity instead.
        if not settings.get("api_key") or "localhost" in settings.get("api_base_url", ""):
            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    novel = await session.get(Novel, ch.novel_id)
                    novel_title = novel.title if novel else ""
                    task = TranslationTask(
                        novel_id=ch.novel_id,
                        novel_title=novel_title,
                        chapter_index=ch.chapter_index,
                        chapter_count=1,
                        status="pending",
                        notes=f"Yêu cầu từ Reader trực tiếp (Chương {ch.chapter_index})"
                    )
                    session.add(task)
                    ch.translation_status = "pending"
                    ch.error_message = None
                    await session.commit()
            
            notice = (
                f"📋 Đã gửi Chương {chapter.chapter_index} vào Hàng đợi dịch của Antigravity!\n\n"
                "👉 Bạn chỉ cần gửi tin nhắn: 'Dịch tiếp chương này' trong chat Antigravity, "
                "tôi sẽ dịch ngay với Gemini 3.8 Flash và nạp thẳng vào đây cho bạn.\n\n"
                "(Hoặc nếu muốn hệ thống tự động dịch realtime trên web mà không cần qua chat, bạn có thể dán Gemini API Key miễn phí tại Cài đặt ⚙️)"
            )
            yield f"data: {json.dumps({'chunk': notice, 'done': True, 'needs_antigravity': True, 'title_translated': chapter.title})}\n\n"
            return

        glossary_prompt = self.build_glossary_prompt(
            f"{chapter.title}\n{chapter.raw_content}", glossary_items
        )

        user_content = (
            f"Hãy dịch tiêu đề và toàn bộ nội dung chương sau đây sang tiếng Việt tiểu thuyết mượt mà, giữ tương ứng đoạn văn:\n\n"
            f"[TIÊU ĐỀ GỐC]: {chapter.title}\n\n"
            f"[NỘI DUNG GỐC]:\n{chapter.raw_content}"
            f"{glossary_prompt}"
        )

        headers = {"Content-Type": "application/json"}
        if settings["api_key"]:
            headers["Authorization"] = f"Bearer {settings['api_key']}"

        payload = {
            "model": settings["model_name"],
            "messages": [
                {"role": "system", "content": settings["system_prompt"]},
                {"role": "user", "content": user_content}
            ],
            "temperature": settings["temperature"],
            "stream": True
        }

        base_url = settings["api_base_url"].rstrip("/")
        url = f"{base_url}/chat/completions"
        full_text = []

        try:
            async with httpx.AsyncClient(timeout=300.0) as client:
                async with client.stream("POST", url, json=payload, headers=headers) as resp:
                    if resp.status_code != 200:
                        err_text = await resp.aread()
                        yield f"data: {json.dumps({'error': f'HTTP {resp.status_code}: {err_text.decode()}'})}\n\n"
                        return

                    async for line in resp.aiter_lines():
                        if not line or not line.startswith("data:"):
                            continue
                        line_data = line[5:].strip()
                        if line_data == "[DONE]":
                            break
                        try:
                            chunk_obj = json.loads(line_data)
                            delta = chunk_obj["choices"][0].get("delta", {})
                            content_piece = delta.get("content", "")
                            if content_piece:
                                full_text.append(content_piece)
                                yield f"data: {json.dumps({'chunk': content_piece, 'done': False})}\n\n"
                        except Exception:
                            continue

            complete_translation = "".join(full_text).strip()
            lines = [l.strip() for l in complete_translation.splitlines() if l.strip()]
            trans_title = lines[0].replace("[TIÊU ĐỀ DỊCH]:", "").replace("[TIÊU ĐỀ]:", "").strip() if lines else chapter.title

            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    ch.translated_content = complete_translation
                    ch.title_translated = trans_title
                    ch.translation_status = "completed"
                    ch.error_message = None
                    await session.commit()

            yield f"data: {json.dumps({'done': True, 'title_translated': trans_title})}\n\n"

        except Exception as e:
            err_msg = str(e)
            if "All connection attempts failed" in err_msg or "Connect call failed" in err_msg or "WinError 10061" in err_msg:
                err_msg = (
                    "Không thể kết nối đến máy chủ AI API đã cấu hình. "
                    "Vui lòng kiểm tra lại đường dẫn API Base URL và API Key trong mục Cài đặt (⚙️), "
                    "hoặc yêu cầu Antigravity dịch trực tiếp bằng Gemini 3.8 Flash."
                )
            async with AsyncSessionLocal() as session:
                ch = await session.get(Chapter, chapter_id)
                if ch:
                    ch.translation_status = "failed"
                    ch.error_message = err_msg
                    await session.commit()
            yield f"data: {json.dumps({'error': err_msg, 'done': True})}\n\n"

    async def enqueue_prefetch(self, novel_id: int, current_index: int, prefetch_count: int = 2):
        """Enqueue next N chapters for background translation when user reads current chapter"""
        async with AsyncSessionLocal() as session:
            target_indices = [current_index + i for i in range(1, prefetch_count + 1)]
            result = await session.execute(
                select(Chapter).where(
                    Chapter.novel_id == novel_id,
                    Chapter.chapter_index.in_(target_indices)
                )
            )
            chapters = result.scalars().all()
            for ch in chapters:
                if ch.translation_status not in ["completed", "translating"] and ch.id not in self.active_tasks:
                    self.active_tasks.add(ch.id)
                    await self.queue.put(ch.id)
                    logger.info(f"Enqueued prefetch for Chapter {ch.chapter_index} (id={ch.id})")

    async def enqueue_chapter(self, chapter_id: int):
        if chapter_id not in self.active_tasks:
            self.active_tasks.add(chapter_id)
            await self.queue.put(chapter_id)

    async def _process_queue(self):
        """Background translation worker loop"""
        while self._is_running:
            try:
                chapter_id = await self.queue.get()
                try:
                    logger.info(f"Background translating chapter_id={chapter_id}")
                    await self.translate_chapter(chapter_id)
                except Exception as e:
                    logger.warning(f"Background translation failed for chapter {chapter_id}: {e}")
                finally:
                    self.active_tasks.discard(chapter_id)
                    self.queue.task_done()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in translation queue worker: {e}")
                await asyncio.sleep(2)

    async def extract_glossary_terms(self, text_sample: str) -> List[Dict[str, str]]:
        """Ask LLM to extract proper nouns, characters, cultivation realms, and recommend Sino-Vietnamese translation"""
        settings = await self.get_ai_settings()

        prompt = f"""Bạn là một chuyên gia dịch thuật tiểu thuyết Trung - Việt và am hiểu sâu sắc về dịch Hán Việt.
Dưới đây là một đoạn trích tiểu thuyết tiếng Trung. Hãy phân tích và trích xuất danh sách các thực thể đặc trưng:
1. Tên nhân vật (nhan_vat)
2. Cảnh giới tu luyện / Công pháp / Chiêu thức (canh_gioi / cong_phap)
3. Địa danh / Môn phái / Thế lực (dia_danh)
4. Pháp bảo / Linh đan / Vật phẩm (vat_pham)

YÊU CẦU ĐẦU RA:
- Trả về DUY NHẤT một mảng JSON thuần túy (không bọc trong markdown code block, không có lời dẫn).
- Mỗi phần tử có cấu trúc:
  {{
    "source_term": "Từ gốc tiếng Trung",
    "target_term": "Dịch Hán Việt chuẩn xác",
    "category": "nhan_vat | canh_gioi | cong_phap | dia_danh | vat_pham | khac",
    "context": "Mô tả ngắn gọn trong ngữ cảnh"
  }}

ĐOẠN VĂN BẢN TRUNG QUỐC:
{text_sample[:3000]}
"""
        headers = {"Content-Type": "application/json"}
        if settings["api_key"]:
            headers["Authorization"] = f"Bearer {settings['api_key']}"

        payload = {
            "model": settings["model_name"],
            "messages": [
                {"role": "system", "content": "Bạn là chuyên gia phân tích văn bản và từ vựng Hán Việt."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2,
            "stream": False
        }

        base_url = settings["api_base_url"].rstrip("/")
        url = f"{base_url}/chat/completions"

        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(url, json=payload, headers=headers)
            if resp.status_code != 200:
                raise ValueError(f"AI API error: {resp.status_code} - {resp.text}")

            content = resp.json()["choices"][0]["message"]["content"].strip()
            # Clean markdown codeblocks if model returned ```json ... ```
            if content.startswith("```"):
                content = content.split("\n", 1)[1]
                if content.endswith("```"):
                    content = content.rsplit("\n", 1)[0]
                content = content.replace("```json", "").replace("```", "").strip()

            try:
                data = json.loads(content)
                if isinstance(data, list):
                    return data
                elif isinstance(data, dict) and "terms" in data:
                    return data["terms"]
                return []
            except Exception:
                return []

translation_service = TranslationService()

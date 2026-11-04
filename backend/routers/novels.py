import os
import shutil
import asyncio
import urllib.parse
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, BackgroundTasks, Response
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db, AsyncSessionLocal
from backend.models import Novel, Chapter, Glossary, ScraperRule
from backend.schemas import (
    NovelResponse,
    NovelCreateFromUrl,
    NovelCreateFromRaw,
    NovelProgressUpdate,
    BulkScrapeRequest,
)
from backend.scraper import (
    scrape_novel_info_and_chapters,
    scrape_single_chapter,
    parse_raw_text_into_chapters,
    extract_domain
)
from backend.translator import translation_service

router = APIRouter(prefix="/api/novels", tags=["Novels"])

ACTIVE_SCRAPE_TASKS = {}

async def background_scrape_all_chapters(novel_id: int, chapters_data: List[dict], rule_dict: Optional[dict] = None):
    """Background task to fetch raw content for chapters that have URLs"""
    async with AsyncSessionLocal() as session:
        for item in chapters_data:
            ch_url = item.get("url")
            ch_index = item.get("index")
            if not ch_url:
                continue

            try:
                # Check if chapter already has raw content
                result = await session.execute(
                    select(Chapter).where(Chapter.novel_id == novel_id, Chapter.chapter_index == ch_index)
                )
                ch = result.scalar_one_or_none()
                if ch and not ch.raw_content:
                    scraped = await scrape_single_chapter(ch_url, rule=rule_dict)
                    ch.raw_content = scraped.get("raw_content", "")
                    if scraped.get("title") and ch.title.startswith("Chương"):
                        ch.title = scraped.get("title")
                    await session.commit()
            except Exception as e:
                print(f"Error fetching chapter {ch_index} for novel {novel_id}: {e}")

@router.get("", response_model=List[NovelResponse])
async def list_novels(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Novel).order_by(Novel.updated_at.desc()))
    novels = result.scalars().all()

    novel_list = []
    for novel in novels:
        # Count translated & pending chapters
        trans_res = await db.execute(
            select(func.count(Chapter.id)).where(
                Chapter.novel_id == novel.id,
                Chapter.translation_status == "completed"
            )
        )
        translated_count = trans_res.scalar() or 0

        pending_res = await db.execute(
            select(func.count(Chapter.id)).where(
                Chapter.novel_id == novel.id,
                Chapter.translation_status != "completed"
            )
        )
        pending_count = pending_res.scalar() or 0

        n_dict = {
            "id": novel.id,
            "title": novel.title,
            "author": novel.author,
            "cover_url": novel.cover_url or "",
            "source_url": novel.source_url or "",
            "description": novel.description or "",
            "genre": novel.genre or "Tiểu thuyết",
            "total_chapters": novel.total_chapters,
            "last_read_chapter_id": novel.last_read_chapter_id,
            "last_read_index": novel.last_read_index,
            "scroll_position": novel.scroll_position,
            "translated_count": translated_count,
            "pending_count": pending_count,
            "created_at": novel.created_at,
            "updated_at": novel.updated_at,
        }
        novel_list.append(NovelResponse(**n_dict))

    return novel_list

@router.get("/{novel_id}", response_model=NovelResponse)
async def get_novel(novel_id: int, db: AsyncSession = Depends(get_db)):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    trans_res = await db.execute(
        select(func.count(Chapter.id)).where(
            Chapter.novel_id == novel.id,
            Chapter.translation_status == "completed"
        )
    )
    translated_count = trans_res.scalar() or 0

    pending_res = await db.execute(
        select(func.count(Chapter.id)).where(
            Chapter.novel_id == novel.id,
            Chapter.translation_status != "completed"
        )
    )
    pending_count = pending_res.scalar() or 0

    return NovelResponse(
        id=novel.id,
        title=novel.title,
        author=novel.author,
        cover_url=novel.cover_url or "",
        source_url=novel.source_url or "",
        description=novel.description or "",
        genre=novel.genre or "Tiểu thuyết",
        total_chapters=novel.total_chapters,
        last_read_chapter_id=novel.last_read_chapter_id,
        last_read_index=novel.last_read_index,
        scroll_position=novel.scroll_position,
        translated_count=translated_count,
        pending_count=pending_count,
        created_at=novel.created_at,
        updated_at=novel.updated_at,
    )

@router.post("/scrape", response_model=NovelResponse)
async def create_novel_from_url(
    payload: NovelCreateFromUrl,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    domain = extract_domain(payload.url)
    rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
    rule_obj = rule_res.scalar_one_or_none()
    rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None

    try:
        scraped = await scrape_novel_info_and_chapters(
            payload.url,
            rule=rule_dict,
            auto_detect=payload.auto_detect
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Lỗi khi cào dữ liệu từ URL: {str(e)}")

    info = scraped["info"]
    raw_chapters = scraped["chapters"]

    if payload.max_chapters and payload.max_chapters > 0:
        raw_chapters = raw_chapters[:payload.max_chapters]

    novel = Novel(
        title=info["title"],
        author=info["author"],
        cover_url=info.get("cover_url", ""),
        source_url=scraped["source_url"],
        description=info.get("description", ""),
        total_chapters=len(raw_chapters),
        last_read_index=1
    )
    db.add(novel)
    await db.flush()

    # Pre-populate chapter records
    chapter_tasks = []
    first_chapter_id = None
    for idx, ch_item in enumerate(raw_chapters, start=1):
        ch = Chapter(
            novel_id=novel.id,
            chapter_index=idx,
            title=ch_item["title"],
            source_url=ch_item["url"],
            translation_status="pending"
        )
        db.add(ch)
        await db.flush()
        if idx == 1:
            first_chapter_id = ch.id
        chapter_tasks.append({"index": idx, "url": ch_item["url"]})

    if first_chapter_id:
        novel.last_read_chapter_id = first_chapter_id

    await db.commit()
    await db.refresh(novel)

    # Scrape first 3 chapters immediately so user can read right away
    async def fetch_initial_and_background():
        async with AsyncSessionLocal() as session:
            for item in chapter_tasks[:3]:
                try:
                    res = await session.execute(
                        select(Chapter).where(Chapter.novel_id == novel.id, Chapter.chapter_index == item["index"])
                    )
                    c = res.scalar_one_or_none()
                    if c and not c.raw_content:
                        scraped_ch = await scrape_single_chapter(item["url"], rule=rule_dict)
                        c.raw_content = scraped_ch.get("raw_content", "")
                        await session.commit()
                except Exception as err:
                    print(f"Initial scrape error: {err}")

        # Continue background scraping for remaining
        await background_scrape_all_chapters(novel.id, chapter_tasks[3:], rule_dict)

    background_tasks.add_task(fetch_initial_and_background)

    return NovelResponse(
        id=novel.id,
        title=novel.title,
        author=novel.author,
        cover_url=novel.cover_url or "",
        source_url=novel.source_url or "",
        description=novel.description or "",
        genre=novel.genre or "Tiểu thuyết",
        total_chapters=novel.total_chapters,
        last_read_chapter_id=novel.last_read_chapter_id,
        last_read_index=novel.last_read_index,
        scroll_position=novel.scroll_position,
        translated_count=0,
        pending_count=novel.total_chapters,
        created_at=novel.created_at,
        updated_at=novel.updated_at,
    )

@router.post("/raw", response_model=NovelResponse)
async def create_novel_from_raw(
    payload: NovelCreateFromRaw,
    db: AsyncSession = Depends(get_db)
):
    if not payload.raw_text.strip():
        raise HTTPException(status_code=400, detail="Văn bản tiếng Trung không được để trống")

    parsed_chapters = parse_raw_text_into_chapters(payload.raw_text)
    if not parsed_chapters:
        raise HTTPException(status_code=400, detail="Không thể tách chương từ văn bản cung cấp")

    novel = Novel(
        title=payload.title.strip(),
        author=payload.author or "Chưa rõ",
        description=payload.description or "",
        source_url="Nhập thủ công",
        total_chapters=len(parsed_chapters),
        last_read_index=1
    )
    db.add(novel)
    await db.flush()

    first_id = None
    for idx, ch_data in enumerate(parsed_chapters, start=1):
        ch = Chapter(
            novel_id=novel.id,
            chapter_index=idx,
            title=ch_data["title"],
            raw_content=ch_data["raw_content"],
            translation_status="pending"
        )
        db.add(ch)
        await db.flush()
        if idx == 1:
            first_id = ch.id

    novel.last_read_chapter_id = first_id
    await db.commit()
    await db.refresh(novel)

    return NovelResponse(
        id=novel.id,
        title=novel.title,
        author=novel.author,
        cover_url="",
        source_url=novel.source_url,
        description=novel.description,
        genre=novel.genre,
        total_chapters=novel.total_chapters,
        last_read_chapter_id=novel.last_read_chapter_id,
        last_read_index=novel.last_read_index,
        scroll_position=0.0,
        translated_count=0,
        pending_count=len(parsed_chapters),
        created_at=novel.created_at,
        updated_at=novel.updated_at,
    )

@router.post("/upload", response_model=NovelResponse)
async def upload_txt_novel(
    title: str = Form(...),
    author: str = Form("Chưa rõ"),
    description: str = Form(""),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    content_bytes = await file.read()
    # Decode text
    from backend.scraper import detect_and_decode
    text = detect_and_decode(content_bytes)

    if not text.strip():
        raise HTTPException(status_code=400, detail="File tải lên không có nội dung văn bản hợp lệ")

    parsed_chapters = parse_raw_text_into_chapters(text)
    novel = Novel(
        title=title.strip() or file.filename.replace(".txt", ""),
        author=author or "Chưa rõ",
        description=description or f"File gốc: {file.filename}",
        source_url=f"Tải lên file: {file.filename}",
        total_chapters=len(parsed_chapters),
        last_read_index=1
    )
    db.add(novel)
    await db.flush()

    first_id = None
    for idx, ch_data in enumerate(parsed_chapters, start=1):
        ch = Chapter(
            novel_id=novel.id,
            chapter_index=idx,
            title=ch_data["title"],
            raw_content=ch_data["raw_content"],
            translation_status="pending"
        )
        db.add(ch)
        await db.flush()
        if idx == 1:
            first_id = ch.id

    novel.last_read_chapter_id = first_id
    await db.commit()
    await db.refresh(novel)

    return NovelResponse(
        id=novel.id,
        title=novel.title,
        author=novel.author,
        cover_url="",
        source_url=novel.source_url,
        description=novel.description,
        genre=novel.genre,
        total_chapters=novel.total_chapters,
        last_read_chapter_id=novel.last_read_chapter_id,
        last_read_index=novel.last_read_index,
        scroll_position=0.0,
        translated_count=0,
        pending_count=len(parsed_chapters),
        created_at=novel.created_at,
        updated_at=novel.updated_at,
    )

@router.put("/{novel_id}/progress")
async def update_reading_progress(
    novel_id: int,
    payload: NovelProgressUpdate,
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    if payload.last_read_chapter_id is not None:
        novel.last_read_chapter_id = payload.last_read_chapter_id
    if payload.last_read_index is not None:
        novel.last_read_index = payload.last_read_index
    if payload.scroll_position is not None:
        novel.scroll_position = payload.scroll_position

    await db.commit()

    # Trigger prefetch of next chapters
    if payload.last_read_index is not None:
        await translation_service.enqueue_prefetch(novel_id, payload.last_read_index, prefetch_count=2)

    return {"status": "success", "novel_id": novel_id, "last_read_index": novel.last_read_index}

@router.delete("/{novel_id}")
async def delete_novel(novel_id: int, db: AsyncSession = Depends(get_db)):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    await db.delete(novel)
    await db.commit()
    return {"status": "success", "message": f"Đã xóa truyện '{novel.title}'"}

@router.post("/{novel_id}/bulk-scrape")
async def bulk_scrape_chapters(
    novel_id: int,
    payload: BulkScrapeRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    domain = extract_domain(novel.source_url) if novel.source_url else ""
    rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
    rule_obj = rule_res.scalar_one_or_none()
    rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None

    # Query target chapters that lack raw content
    if payload.all_remaining:
        query = select(Chapter).where(
            Chapter.novel_id == novel_id,
            (Chapter.raw_content == None) | (Chapter.raw_content == "")
        ).order_by(Chapter.chapter_index.asc())
    else:
        end_idx = payload.start_index + payload.count - 1
        query = select(Chapter).where(
            Chapter.novel_id == novel_id,
            Chapter.chapter_index >= payload.start_index,
            Chapter.chapter_index <= end_idx,
            (Chapter.raw_content == None) | (Chapter.raw_content == "")
        ).order_by(Chapter.chapter_index.asc())

    res = await db.execute(query)
    target_chapters = res.scalars().all()

    if not target_chapters:
        return {
            "status": "success",
            "novel_id": novel_id,
            "total_targets": 0,
            "message": "Toàn bộ các chương được chọn đã có sẵn nội dung trong máy!"
        }

    ch_tasks = [{"id": ch.id, "url": ch.source_url, "index": ch.chapter_index} for ch in target_chapters if ch.source_url]

    ACTIVE_SCRAPE_TASKS[novel_id] = {
        "total": len(ch_tasks),
        "scraped": 0,
        "status": "running",
        "current_index": ch_tasks[0]["index"]
    }

    async def worker_bulk_scrape():
        sem = asyncio.Semaphore(4)
        async with AsyncSessionLocal() as session:
            for item in ch_tasks:
                async with sem:
                    try:
                        scraped = await scrape_single_chapter(item["url"], rule=rule_dict)
                        ch = await session.get(Chapter, item["id"])
                        if ch:
                            ch.raw_content = scraped.get("raw_content", "")
                            if scraped.get("title") and ch.title.startswith("Chương"):
                                ch.title = scraped.get("title")
                            await session.commit()
                        if novel_id in ACTIVE_SCRAPE_TASKS:
                            ACTIVE_SCRAPE_TASKS[novel_id]["scraped"] += 1
                            ACTIVE_SCRAPE_TASKS[novel_id]["current_index"] = item["index"]
                    except Exception as err:
                        print(f"Error scraping chapter {item['index']}: {err}")
                    await asyncio.sleep(0.2)
            if novel_id in ACTIVE_SCRAPE_TASKS:
                ACTIVE_SCRAPE_TASKS[novel_id]["status"] = "completed"

    background_tasks.add_task(worker_bulk_scrape)

    return {
        "status": "started",
        "novel_id": novel_id,
        "total_targets": len(ch_tasks),
        "message": f"Bắt đầu tải ngầm {len(ch_tasks)} chương về máy cục bộ..."
    }

@router.get("/{novel_id}/scrape-status")
async def get_scrape_status(novel_id: int, db: AsyncSession = Depends(get_db)):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    raw_res = await db.execute(
        select(func.count(Chapter.id)).where(
            Chapter.novel_id == novel_id,
            Chapter.raw_content != None,
            Chapter.raw_content != ""
        )
    )
    raw_count = raw_res.scalar() or 0

    trans_res = await db.execute(
        select(func.count(Chapter.id)).where(
            Chapter.novel_id == novel_id,
            Chapter.translation_status == "completed"
        )
    )
    trans_count = trans_res.scalar() or 0

    return {
        "novel_id": novel_id,
        "total_chapters": novel.total_chapters,
        "raw_count": raw_count,
        "translated_count": trans_count,
        "remaining_raw": max(0, novel.total_chapters - raw_count),
        "raw_percent": round((raw_count / max(1, novel.total_chapters)) * 100, 1),
        "trans_percent": round((trans_count / max(1, novel.total_chapters)) * 100, 1),
        "active_task": ACTIVE_SCRAPE_TASKS.get(novel_id, {"status": "idle"})
    }

@router.get("/{novel_id}/export")
async def export_novel_txt(
    novel_id: int,
    mode: str = "translated",
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    res = await db.execute(
        select(Chapter).where(Chapter.novel_id == novel_id).order_by(Chapter.chapter_index.asc())
    )
    chapters = res.scalars().all()

    lines = [
        f"TÁC PHẨM: {novel.title}",
        f"TÁC GIẢ: {novel.author}",
        f"THỂ LOẠI: {novel.genre}",
        f"NGUỒN GỐC: {novel.source_url}",
        f"TỔNG SỐ CHƯƠNG: {len(chapters)}",
        f"TÓM TẮT: {novel.description}",
        "=" * 60,
        ""
    ]

    for ch in chapters:
        ch_title = ch.title_translated or ch.title or f"Chương {ch.chapter_index}"
        lines.append(f"\n\n{'=' * 20} #Chương {ch.chapter_index}: {ch_title} {'=' * 20}\n")
        if mode == "raw":
            lines.append(ch.raw_content or "[Chưa có nội dung tiếng Trung]")
        elif mode == "bilingual":
            lines.append("[BẢN DỊCH TIẾNG VIỆT]:")
            lines.append(ch.translated_content or "[Chưa dịch]")
            lines.append("\n[BẢN GỐC TIẾNG TRUNG]:")
            lines.append(ch.raw_content or "[Chưa có nội dung tiếng Trung]")
        else: # translated
            if ch.translated_content:
                lines.append(ch.translated_content)
            elif ch.raw_content:
                lines.append(f"[Chương chưa dịch - Nội dung gốc]:\n{ch.raw_content}")
            else:
                lines.append("[Chưa tải nội dung chương này]")

    full_content = "\n".join(lines)
    safe_filename = urllib.parse.quote(f"{novel.title}.txt")
    return Response(
        content=full_content.encode("utf-8"),
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename*=UTF-8''{safe_filename}"}
    )

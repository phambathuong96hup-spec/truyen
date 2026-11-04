import asyncio
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, BackgroundTasks
from fastapi.responses import StreamingResponse
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db, AsyncSessionLocal
from backend.models import Chapter, Novel, Glossary, ScraperRule, TranslationTask
from backend.schemas import (
    ChapterSummaryResponse,
    ChapterDetailResponse,
    ChapterTranslateRequest,
    BatchTranslateRequest,
    GlossaryExtractSuggestion
)
from backend.translator import translation_service
from backend.scraper import scrape_single_chapter, extract_domain

router = APIRouter(tags=["Chapters"])

@router.get("/api/novels/{novel_id}/chapters", response_model=List[ChapterSummaryResponse])
async def list_chapters_of_novel(
    novel_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=5000),
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    query = (
        select(Chapter)
        .where(Chapter.novel_id == novel_id)
        .order_by(Chapter.chapter_index.asc())
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(query)
    chapters = result.scalars().all()
    return chapters

@router.get("/api/chapters/{chapter_id}", response_model=ChapterDetailResponse)
async def get_chapter_detail(
    chapter_id: int,
    prefetch: bool = True,
    db: AsyncSession = Depends(get_db)
):
    chapter = await db.get(Chapter, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Không tìm thấy chương")

    # If raw content is missing but source_url exists, fetch it on-demand
    if not chapter.raw_content and chapter.source_url:
        domain = extract_domain(chapter.source_url)
        rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
        rule_obj = rule_res.scalar_one_or_none()
        rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None

        try:
            scraped = await scrape_single_chapter(chapter.source_url, rule=rule_dict)
            chapter.raw_content = scraped.get("raw_content", "")
            if scraped.get("title") and chapter.title.startswith("Chương"):
                chapter.title = scraped.get("title")
            await db.commit()
        except Exception as e:
            print(f"Error fetching raw content on-demand: {e}")

    # Find prev and next chapters
    prev_res = await db.execute(
        select(Chapter)
        .where(Chapter.novel_id == chapter.novel_id, Chapter.chapter_index < chapter.chapter_index)
        .order_by(Chapter.chapter_index.desc())
        .limit(1)
    )
    prev_chapter = prev_res.scalar_one_or_none()

    next_res = await db.execute(
        select(Chapter)
        .where(Chapter.novel_id == chapter.novel_id, Chapter.chapter_index > chapter.chapter_index)
        .order_by(Chapter.chapter_index.asc())
        .limit(1)
    )
    next_chapter = next_res.scalar_one_or_none()

    novel = await db.get(Novel, chapter.novel_id)

    # Trigger prefetching for next 2 chapters
    if prefetch:
        await translation_service.enqueue_prefetch(chapter.novel_id, chapter.chapter_index, prefetch_count=2)

    return ChapterDetailResponse(
        id=chapter.id,
        novel_id=chapter.novel_id,
        chapter_index=chapter.chapter_index,
        title=chapter.title,
        title_translated=chapter.title_translated or "",
        source_url=chapter.source_url or "",
        raw_content=chapter.raw_content or "",
        translated_content=chapter.translated_content or "",
        translation_status=chapter.translation_status,
        error_message=chapter.error_message,
        prev_id=prev_chapter.id if prev_chapter else None,
        next_id=next_chapter.id if next_chapter else None,
        prev_index=prev_chapter.chapter_index if prev_chapter else None,
        next_index=next_chapter.chapter_index if next_chapter else None,
        prev_title=(prev_chapter.title_translated or prev_chapter.title) if prev_chapter else None,
        next_title=(next_chapter.title_translated or next_chapter.title) if next_chapter else None,
        novel_title=novel.title if novel else "",
        total_chapters=novel.total_chapters if novel else 0,
    )

@router.post("/api/chapters/{chapter_id}/translate")
async def translate_chapter_endpoint(
    chapter_id: int,
    payload: ChapterTranslateRequest = ChapterTranslateRequest(),
    db: AsyncSession = Depends(get_db)
):
    chapter = await db.get(Chapter, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Không tìm thấy chương")

    # If raw content missing, fetch it first
    if not chapter.raw_content and chapter.source_url:
        domain = extract_domain(chapter.source_url)
        rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
        rule_obj = rule_res.scalar_one_or_none()
        rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None
        scraped = await scrape_single_chapter(chapter.source_url, rule=rule_dict)
        chapter.raw_content = scraped.get("raw_content", "")
        await db.commit()

    try:
        translated_text = await translation_service.translate_chapter(chapter_id, force=payload.force)
        # Refresh to get updated title_translated
        await db.refresh(chapter)
        return {
            "status": "success",
            "chapter_id": chapter_id,
            "title_translated": chapter.title_translated,
            "translated_content": translated_text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi dịch thuật AI: {str(e)}")

@router.get("/api/chapters/{chapter_id}/stream")
async def stream_translate_chapter_endpoint(
    chapter_id: int,
    force: bool = False,
    db: AsyncSession = Depends(get_db)
):
    chapter = await db.get(Chapter, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Không tìm thấy chương")

    # If raw content missing, fetch it first
    if not chapter.raw_content and chapter.source_url:
        domain = extract_domain(chapter.source_url)
        rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
        rule_obj = rule_res.scalar_one_or_none()
        rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None
        scraped = await scrape_single_chapter(chapter.source_url, rule=rule_dict)
        chapter.raw_content = scraped.get("raw_content", "")
        await db.commit()

    return StreamingResponse(
        translation_service.stream_translate_chapter(chapter_id, force=force),
        media_type="text/event-stream"
    )

@router.post("/api/novels/{novel_id}/batch-translate")
async def batch_translate_chapters(
    novel_id: int,
    payload: BatchTranslateRequest,
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    novel_title = novel.title if novel else ""
    
    if payload.all_remaining:
        query = (
            select(Chapter)
            .where(
                Chapter.novel_id == novel_id,
                Chapter.translation_status != "completed"
            )
            .order_by(Chapter.chapter_index.asc())
        )
    else:
        end_index = payload.start_index + payload.count - 1
        query = (
            select(Chapter)
            .where(
                Chapter.novel_id == novel_id,
                Chapter.chapter_index >= payload.start_index,
                Chapter.chapter_index <= end_index,
                Chapter.translation_status != "completed"
            )
            .order_by(Chapter.chapter_index.asc())
        )
    result = await db.execute(query)
    chapters = result.scalars().all()

    if not chapters:
        return {
            "status": "success",
            "novel_id": novel_id,
            "enqueued_count": 0,
            "message": "Không có chương nào cần dịch theo yêu cầu"
        }

    # Reset any failed chapters to clean pending state
    for ch in chapters:
        if ch.translation_status == "failed":
            ch.translation_status = "pending"
            ch.error_message = None

    actual_start = chapters[0].chapter_index
    actual_count = len(chapters)

    note_text = (
        f"Yêu cầu dịch TOÀN BỘ {actual_count} chương còn lại (bắt đầu từ Ch. {actual_start})"
        if payload.all_remaining else
        f"Yêu cầu dịch {actual_count} chương (từ Ch. {actual_start} đến {chapters[-1].chapter_index})"
    )

    # Register batch task into TranslationTask for Antigravity
    batch_task = TranslationTask(
        novel_id=novel_id,
        novel_title=novel_title,
        chapter_index=actual_start,
        chapter_count=actual_count,
        status="pending",
        notes=note_text
    )
    db.add(batch_task)
    await db.commit()

    enqueued_count = 0
    for ch in chapters:
        await translation_service.enqueue_chapter(ch.id)
        enqueued_count += 1

    return {
        "status": "success",
        "novel_id": novel_id,
        "task_id": batch_task.id,
        "enqueued_count": enqueued_count,
        "message": f"Đã gửi {enqueued_count} chương vào Hàng đợi dịch của Antigravity (Task #{batch_task.id})!"
    }

@router.post("/api/chapters/{chapter_id}/extract-glossary", response_model=List[GlossaryExtractSuggestion])
async def extract_glossary_from_chapter(
    chapter_id: int,
    db: AsyncSession = Depends(get_db)
):
    chapter = await db.get(Chapter, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Không tìm thấy chương")

    sample_text = f"{chapter.title}\n{chapter.raw_content}"
    if not sample_text.strip():
        raise HTTPException(status_code=400, detail="Chương chưa có nội dung gốc")

    try:
        suggestions = await translation_service.extract_glossary_terms(sample_text)
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi trích xuất thực thể AI: {str(e)}")

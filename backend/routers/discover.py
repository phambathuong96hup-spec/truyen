from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, BackgroundTasks
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db, AsyncSessionLocal
from backend.models import Novel, Chapter, Glossary, ScraperRule
from backend.discover import DISCOVER_CATEGORIES, CURATED_NOVELS, get_catalog_novels, load_live_web_novels
from backend.scraper import scrape_novel_info_and_chapters, scrape_single_chapter, extract_domain
from backend.translator import translation_service
from backend.hanviet import to_sino_vietnamese

router = APIRouter(prefix="/api/discover", tags=["Discover & Clone"])

class CloneRequest(BaseModel):
    catalog_id: str
    auto_translate_first: int = 3
    source_url: Optional[str] = None
    title: Optional[str] = None
    title_vi: Optional[str] = None
    author: Optional[str] = None
    cover_url: Optional[str] = None
    category: Optional[str] = None

@router.get("/categories")
async def list_categories():
    live_novels = load_live_web_novels()
    from collections import Counter
    counts = Counter(n.get("category", "") for n in live_novels)
    curated_counts = Counter(n.get("category", "") for n in CURATED_NOVELS)

    enriched_cats = []
    for cat in DISCOVER_CATEGORIES:
        cid = cat["id"]
        if cid == "all":
            total_cnt = len(CURATED_NOVELS) + len(live_novels)
        else:
            total_cnt = counts.get(cid, 0) + curated_counts.get(cid, 0)
        enriched_cats.append({
            **cat,
            "count": total_cnt
        })
    return enriched_cats

@router.get("/stats")
async def get_discover_stats():
    live_novels = load_live_web_novels()
    return {
        "curated_total": len(CURATED_NOVELS),
        "live_total": len(live_novels),
        "total_available": len(CURATED_NOVELS) + len(live_novels)
    }

@router.get("/novels")
async def list_discover_novels(
    category: str = Query("all"),
    sort_by: str = Query("hot"), # hot, views, rating, chapters
    time_range: str = Query("all"), # all, week, month, year
    source_mode: str = Query("all"), # "curated", "live", "all"
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(24, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    catalog_res = get_catalog_novels(
        category=category,
        sort_by=sort_by,
        time_range=time_range,
        search=search,
        source_mode=source_mode,
        page=page,
        page_size=page_size
    )
    catalog_items = catalog_res["items"]

    # Check which novels are already downloaded in local SQLite database
    local_res = await db.execute(select(Novel.id, Novel.title, Novel.source_url))
    local_novels = local_res.all()
    downloaded_sources = {n.source_url: n.id for n in local_novels if n.source_url}
    downloaded_titles = {n.title.lower(): n.id for n in local_novels}

    enriched = []
    for item in catalog_items:
        local_id = (
            downloaded_sources.get(item.get("source_url")) or
            downloaded_titles.get(item.get("title_vi", "").lower()) or
            downloaded_titles.get(item.get("title", "").lower())
        )
        enriched.append({
            **item,
            "is_downloaded": local_id is not None,
            "local_novel_id": local_id
        })

    return {
        "total": catalog_res["total"],
        "page": catalog_res["page"],
        "page_size": catalog_res["page_size"],
        "has_more": catalog_res["has_more"],
        "items": enriched
    }

@router.get("/novel/{catalog_id}")
async def get_discover_novel_detail(
    catalog_id: str,
    db: AsyncSession = Depends(get_db)
):
    """View full novel synopsis and detail without needing to download/clone it"""
    # 1. Search in curated novels
    novel = next((n for n in CURATED_NOVELS if n["id"] == catalog_id), None)
    
    # 2. Search in live web novels cache
    if not novel:
        live_list = load_live_web_novels()
        novel = next((n for n in live_list if n["id"] == catalog_id), None)

    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện trong kho online")

    from backend.discover import enrich_novel_metrics
    enriched_novel = enrich_novel_metrics(dict(novel))

    # Check if downloaded
    local_res = await db.execute(select(Novel.id).where(Novel.source_url == novel.get("source_url")))
    local_id = local_res.scalar_one_or_none()
    if not local_id:
        local_title_res = await db.execute(select(Novel.id).where(Novel.title == novel.get("title_vi")))
        local_id = local_title_res.scalar_one_or_none()

    enriched_novel["is_downloaded"] = local_id is not None
    enriched_novel["local_novel_id"] = local_id
    return enriched_novel

@router.post("/clone")
async def clone_and_download_novel(
    payload: CloneRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    """Clone online novel to local SQLite database and queue auto-translation"""
    # 1. Search in curated novels
    target_novel = next((n for n in CURATED_NOVELS if n["id"] == payload.catalog_id), None)
    
    # 2. Search in live web novels cache
    if not target_novel:
        live_list = load_live_web_novels()
        target_novel = next((n for n in live_list if n["id"] == payload.catalog_id), None)

    # 3. Fallback to payload metadata if provided
    if not target_novel and payload.source_url:
        t_vi = payload.title_vi or to_sino_vietnamese(payload.title or "") or payload.title or "Tiểu thuyết mạng"
        target_novel = {
            "id": payload.catalog_id,
            "title": payload.title or "Tiểu thuyết mạng",
            "title_vi": t_vi,
            "author": payload.author or "Chưa rõ",
            "author_vi": payload.author or "Chưa rõ",
            "cover_url": payload.cover_url or "",
            "source_url": payload.source_url,
            "source_domain": extract_domain(payload.source_url),
            "description_vi": f"Tiểu thuyết {t_vi}",
            "category": payload.category or "huyen_huyen",
            "category_name": "Tiên Hiệp / Huyền Huyễn",
            "total_chapters": 500
        }

    if not target_novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện trong danh mục khám phá")

    # Check if already cloned
    existing_res = await db.execute(
        select(Novel).where(
            (Novel.source_url == target_novel["source_url"]) | 
            (Novel.title == target_novel["title_vi"]) |
            (Novel.title == target_novel["title"])
        )
    )
    existing = existing_res.scalar_one_or_none()
    if existing:
        return {
            "status": "already_exists",
            "message": "Truyện đã có sẵn trong thư viện máy",
            "novel_id": existing.id,
            "novel_title": existing.title
        }

    # Scrape novel table of contents and info from the live Chinese source URL
    domain = extract_domain(target_novel["source_url"])
    rule_res = await db.execute(select(ScraperRule).where(ScraperRule.domain == domain))
    rule_obj = rule_res.scalar_one_or_none()
    rule_dict = {c.name: getattr(rule_obj, c.name) for c in ScraperRule.__table__.columns} if rule_obj else None

    try:
        scraped = await scrape_novel_info_and_chapters(target_novel["source_url"], rule=rule_dict, auto_detect=True)
    except Exception as e:
        # Fallback to simulated chapters if site is blocked
        scraped = {
            "info": {
                "title": target_novel["title"],
                "author": target_novel["author"],
                "cover_url": target_novel["cover_url"],
                "description": target_novel["description_vi"]
            },
            "chapters": [
                {"title": f"第{i}章", "url": f"{target_novel['source_url']}{i}.html"}
                for i in range(1, min(100, target_novel.get("total_chapters", 100) + 1))
            ],
            "source_url": target_novel["source_url"]
        }

    chapters_list = scraped.get("chapters", [])
    if not chapters_list:
        chapters_list = [
            {"title": f"第{i}章", "url": f"{target_novel['source_url']}{i}.html"}
            for i in range(1, 50)
        ]

    final_title_vi = target_novel.get("title_vi") or to_sino_vietnamese(scraped.get("info", {}).get("title", ""))
    scraped_author = scraped.get("info", {}).get("author") or target_novel.get("author", "Chưa rõ")
    author_display = f"{target_novel.get('author_vi', scraped_author)} ({scraped_author})" if target_novel.get('author_vi') else scraped_author
    cover_display = scraped.get("info", {}).get("cover_url") or target_novel.get("cover_url", "")
    desc_display = target_novel.get("description_vi") or scraped.get("info", {}).get("description", "")

    novel = Novel(
        title=final_title_vi,
        author=author_display,
        cover_url=cover_display,
        source_url=scraped.get("source_url", target_novel["source_url"]),
        description=desc_display,
        genre=target_novel.get("category_name", "Tiên Hiệp"),
        total_chapters=len(chapters_list),
        last_read_index=1
    )
    db.add(novel)
    await db.flush()

    # Pre-populate chapter records
    first_chapter_id = None
    initial_scrape_tasks = []
    for idx, ch_item in enumerate(chapters_list, start=1):
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
        if idx <= payload.auto_translate_first:
            initial_scrape_tasks.append({"id": ch.id, "url": ch_item["url"], "index": idx})

    novel.last_read_chapter_id = first_chapter_id

    # Add initial glossary for main terms
    db.add(Glossary(
        novel_id=novel.id,
        source_term=target_novel.get("author", "作者"),
        target_term=target_novel.get("author_vi", "Tác giả"),
        category="nhan_vat",
        notes="Tác giả"
    ))
    db.add(Glossary(
        novel_id=novel.id,
        source_term=target_novel["title"],
        target_term=final_title_vi,
        category="khac",
        notes="Tiêu đề truyện"
    ))

    await db.commit()
    await db.refresh(novel)

    # Background task to fetch raw content and start translating initial chapters
    async def initial_clone_and_translate_worker():
        async with AsyncSessionLocal() as session:
            for item in initial_scrape_tasks:
                try:
                    ch = await session.get(Chapter, item["id"])
                    if ch and not ch.raw_content and ch.source_url:
                        scraped_ch = await scrape_single_chapter(ch.source_url, rule=rule_dict)
                        ch.raw_content = scraped_ch.get("raw_content", "")
                        await session.commit()
                        # Enqueue for translation
                        await translation_service.enqueue_chapter(ch.id)
                except Exception as err:
                    print(f"Error scraping/translating cloned chapter {item['index']}: {err}")

    background_tasks.add_task(initial_clone_and_translate_worker)

    return {
        "status": "success",
        "message": f"Đã clone thành công truyện '{novel.title}' về máy!",
        "novel_id": novel.id,
        "novel_title": novel.title,
        "first_chapter_id": first_chapter_id,
        "total_chapters": novel.total_chapters
    }

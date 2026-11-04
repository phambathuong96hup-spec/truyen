from typing import List
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.models import ScraperRule
from backend.schemas import ScraperRuleCreate, ScraperRuleResponse
from backend.scraper import scrape_novel_info_and_chapters, scrape_single_chapter, extract_domain

router = APIRouter(prefix="/api/scraper-rules", tags=["Scraper Rules"])

class TestRulePayload(BaseModel):
    url: str
    rule: ScraperRuleCreate

@router.get("", response_model=List[ScraperRuleResponse])
async def list_scraper_rules(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ScraperRule).order_by(ScraperRule.domain.asc()))
    return result.scalars().all()

@router.post("", response_model=ScraperRuleResponse)
async def create_scraper_rule(payload: ScraperRuleCreate, db: AsyncSession = Depends(get_db)):
    clean_domain = payload.domain.strip().lower()
    if clean_domain.startswith("www."):
        clean_domain = clean_domain[4:]

    existing = await db.execute(select(ScraperRule).where(ScraperRule.domain == clean_domain))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail=f"Quy tắc cho domain '{clean_domain}' đã tồn tại")

    rule = ScraperRule(
        domain=clean_domain,
        name=payload.name.strip(),
        novel_title_selector=payload.novel_title_selector,
        novel_author_selector=payload.novel_author_selector,
        novel_cover_selector=payload.novel_cover_selector,
        novel_desc_selector=payload.novel_desc_selector,
        chapter_list_selector=payload.chapter_list_selector,
        chapter_link_selector=payload.chapter_link_selector,
        chapter_title_selector=payload.chapter_title_selector,
        chapter_content_selector=payload.chapter_content_selector,
        content_remove_selectors=payload.content_remove_selectors,
        encoding=payload.encoding or "auto"
    )
    db.add(rule)
    await db.commit()
    await db.refresh(rule)
    return rule

@router.put("/{rule_id}", response_model=ScraperRuleResponse)
async def update_scraper_rule(rule_id: int, payload: ScraperRuleCreate, db: AsyncSession = Depends(get_db)):
    rule = await db.get(ScraperRule, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Không tìm thấy quy tắc cào")

    rule.name = payload.name.strip()
    rule.novel_title_selector = payload.novel_title_selector
    rule.novel_author_selector = payload.novel_author_selector
    rule.novel_cover_selector = payload.novel_cover_selector
    rule.novel_desc_selector = payload.novel_desc_selector
    rule.chapter_list_selector = payload.chapter_list_selector
    rule.chapter_link_selector = payload.chapter_link_selector
    rule.chapter_title_selector = payload.chapter_title_selector
    rule.chapter_content_selector = payload.chapter_content_selector
    rule.content_remove_selectors = payload.content_remove_selectors
    rule.encoding = payload.encoding or "auto"

    await db.commit()
    await db.refresh(rule)
    return rule

@router.delete("/{rule_id}")
async def delete_scraper_rule(rule_id: int, db: AsyncSession = Depends(get_db)):
    rule = await db.get(ScraperRule, rule_id)
    if not rule:
        raise HTTPException(status_code=404, detail="Không tìm thấy quy tắc cào")

    await db.delete(rule)
    await db.commit()
    return {"status": "success", "message": f"Đã xóa quy tắc cho domain '{rule.domain}'"}

@router.post("/test")
async def test_scraper_rule(payload: TestRulePayload):
    try:
        rule_dict = payload.rule.model_dump()
        result = await scrape_novel_info_and_chapters(payload.url, rule=rule_dict, auto_detect=False)
        return {
            "status": "success",
            "info": result["info"],
            "chapter_count": len(result["chapters"]),
            "sample_chapters": result["chapters"][:5]
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

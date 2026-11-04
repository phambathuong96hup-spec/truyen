from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.models import Glossary, Novel
from backend.schemas import (
    GlossaryItemCreate,
    GlossaryItemUpdate,
    GlossaryItemResponse,
    GlossaryBulkCreate
)

router = APIRouter(tags=["Glossary"])

@router.get("/api/novels/{novel_id}/glossary", response_model=List[GlossaryItemResponse])
async def list_glossary(
    novel_id: int,
    category: Optional[str] = None,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Glossary).where(Glossary.novel_id == novel_id)

    if category and category != "all":
        query = query.where(Glossary.category == category)

    if search:
        search_pattern = f"%{search}%"
        query = query.where(
            or_(
                Glossary.source_term.ilike(search_pattern),
                Glossary.target_term.ilike(search_pattern)
            )
        )

    query = query.order_by(Glossary.created_at.desc())
    result = await db.execute(query)
    return result.scalars().all()

@router.post("/api/novels/{novel_id}/glossary", response_model=GlossaryItemResponse)
async def create_glossary_item(
    novel_id: int,
    payload: GlossaryItemCreate,
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    # Check if term already exists for this novel
    existing = await db.execute(
        select(Glossary).where(
            Glossary.novel_id == novel_id,
            Glossary.source_term == payload.source_term.strip()
        )
    )
    item = existing.scalar_one_or_none()
    if item:
        item.target_term = payload.target_term.strip()
        item.category = payload.category
        item.notes = payload.notes or item.notes
    else:
        item = Glossary(
            novel_id=novel_id,
            source_term=payload.source_term.strip(),
            target_term=payload.target_term.strip(),
            category=payload.category,
            notes=payload.notes or ""
        )
        db.add(item)

    await db.commit()
    await db.refresh(item)
    return item

@router.post("/api/novels/{novel_id}/glossary/bulk")
async def bulk_create_glossary(
    novel_id: int,
    payload: GlossaryBulkCreate,
    db: AsyncSession = Depends(get_db)
):
    novel = await db.get(Novel, novel_id)
    if not novel:
        raise HTTPException(status_code=404, detail="Không tìm thấy truyện")

    added_count = 0
    updated_count = 0

    for item_data in payload.items:
        src = item_data.source_term.strip()
        tgt = item_data.target_term.strip()
        if not src or not tgt:
            continue

        existing = await db.execute(
            select(Glossary).where(
                Glossary.novel_id == novel_id,
                Glossary.source_term == src
            )
        )
        item = existing.scalar_one_or_none()
        if item:
            item.target_term = tgt
            item.category = item_data.category
            item.notes = item_data.notes or item.notes
            updated_count += 1
        else:
            new_item = Glossary(
                novel_id=novel_id,
                source_term=src,
                target_term=tgt,
                category=item_data.category,
                notes=item_data.notes or ""
            )
            db.add(new_item)
            added_count += 1

    await db.commit()
    return {
        "status": "success",
        "added": added_count,
        "updated": updated_count,
        "total": added_count + updated_count
    }

@router.put("/api/glossary/{glossary_id}", response_model=GlossaryItemResponse)
async def update_glossary_item(
    glossary_id: int,
    payload: GlossaryItemUpdate,
    db: AsyncSession = Depends(get_db)
):
    item = await db.get(Glossary, glossary_id)
    if not item:
        raise HTTPException(status_code=404, detail="Không tìm thấy từ trong từ điển")

    if payload.source_term is not None:
        item.source_term = payload.source_term.strip()
    if payload.target_term is not None:
        item.target_term = payload.target_term.strip()
    if payload.category is not None:
        item.category = payload.category
    if payload.notes is not None:
        item.notes = payload.notes

    await db.commit()
    await db.refresh(item)
    return item

@router.delete("/api/glossary/{glossary_id}")
async def delete_glossary_item(
    glossary_id: int,
    db: AsyncSession = Depends(get_db)
):
    item = await db.get(Glossary, glossary_id)
    if not item:
        raise HTTPException(status_code=404, detail="Không tìm thấy từ trong từ điển")

    await db.delete(item)
    await db.commit()
    return {"status": "success", "message": f"Đã xóa từ '{item.source_term}'"}

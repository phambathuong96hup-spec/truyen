import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.models import TranslationTask, Novel, Chapter

router = APIRouter(prefix="/api/queue", tags=["Translation Queue"])

class CreateTaskRequest(BaseModel):
    novel_id: int
    chapter_index: int
    chapter_count: int = 1
    novel_title: Optional[str] = ""

class TaskResponse(BaseModel):
    id: int
    novel_id: int
    novel_title: str
    chapter_index: int
    chapter_count: int
    status: str
    notes: Optional[str]
    created_at: datetime.datetime
    completed_at: Optional[datetime.datetime]

    class Config:
        from_attributes = True

@router.post("/request", response_model=TaskResponse)
async def create_translation_task(
    payload: CreateTaskRequest,
    db: AsyncSession = Depends(get_db)
):
    """Called from Web UI when user clicks 'Dịch chương này' or 'Dịch tiếp'"""
    # Fetch novel title if not provided
    title = payload.novel_title
    if not title:
        novel_res = await db.execute(select(Novel.title).where(Novel.id == payload.novel_id))
        title = novel_res.scalar_one_or_none() or f"Truyện #{payload.novel_id}"

    task = TranslationTask(
        novel_id=payload.novel_id,
        novel_title=title,
        chapter_index=payload.chapter_index,
        chapter_count=payload.chapter_count,
        status="pending",
        notes=f"Yêu cầu từ Web Reader lúc {datetime.datetime.now().strftime('%H:%M:%S')}"
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

@router.get("", response_model=List[TaskResponse])
async def list_tasks(
    status: Optional[str] = None,
    limit: int = 20,
    db: AsyncSession = Depends(get_db)
):
    """List translation tasks (used by Antigravity or UI)"""
    stmt = select(TranslationTask)
    if status:
        stmt = stmt.where(TranslationTask.status == status)
    stmt = stmt.order_by(desc(TranslationTask.created_at)).limit(limit)
    res = await db.execute(stmt)
    return res.scalars().all()

@router.post("/{task_id}/complete")
async def complete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Mark a task completed once Antigravity or server finishes translation"""
    res = await db.execute(select(TranslationTask).where(TranslationTask.id == task_id))
    task = res.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task không tồn tại")
    task.status = "completed"
    task.completed_at = datetime.datetime.utcnow()
    await db.commit()
    return {"status": "success", "task_id": task_id}

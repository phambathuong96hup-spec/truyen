from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel
from sqlalchemy import select
from backend.database import AsyncSessionLocal
from backend.models import AppSetting
from backend.config import APP_PASSCODE

router = APIRouter(prefix="/api/auth", tags=["Auth"])

class VerifyRequest(BaseModel):
    passcode: str

class SetPasscodeRequest(BaseModel):
    old_passcode: str = ""
    new_passcode: str

async def get_active_passcode() -> str:
    """Get active passcode: Env var takes precedence, fallback to DB AppSetting."""
    if APP_PASSCODE:
        return APP_PASSCODE
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(AppSetting).where(AppSetting.key == "app_passcode"))
        setting = result.scalars().first()
        if setting and setting.value:
            return setting.value.strip()
    return ""

@router.get("/status")
async def auth_status():
    passcode = await get_active_passcode()
    return {
        "requires_passcode": bool(passcode),
        "is_env_locked": bool(APP_PASSCODE)
    }

@router.post("/verify")
async def verify_passcode(payload: VerifyRequest):
    active_passcode = await get_active_passcode()
    if not active_passcode:
        return {"valid": True, "message": "Không yêu cầu mật khẩu"}
    
    if payload.passcode == active_passcode:
        return {"valid": True, "message": "Xác thực thành công"}
    
    raise HTTPException(status_code=401, detail="Mật khẩu bảo mật không chính xác")

@router.post("/set-passcode")
async def set_passcode(payload: SetPasscodeRequest):
    if APP_PASSCODE:
        raise HTTPException(
            status_code=400, 
            detail="Mật khẩu đang được khóa cố định qua biến môi trường máy chủ (APP_PASSCODE). Vui lòng đổi trong bảng điều khiển máy chủ."
        )
    
    active_passcode = await get_active_passcode()
    if active_passcode and payload.old_passcode != active_passcode:
        raise HTTPException(status_code=401, detail="Mật khẩu cũ không chính xác")
    
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(AppSetting).where(AppSetting.key == "app_passcode"))
        setting = result.scalars().first()
        if not setting:
            setting = AppSetting(key="app_passcode", value=payload.new_passcode.strip())
            session.add(setting)
        else:
            setting.value = payload.new_passcode.strip()
        await session.commit()
        
    return {
        "status": "success", 
        "message": "Đã cập nhật mật khẩu bảo vệ thành công!" if payload.new_passcode else "Đã gỡ bỏ mật khẩu bảo vệ."
    }

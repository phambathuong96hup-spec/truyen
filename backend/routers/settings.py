from fastapi import APIRouter, HTTPException
import httpx
from backend.schemas import SettingsPayload, TestAiRequest
from backend.translator import translation_service

router = APIRouter(prefix="/api/settings", tags=["Settings"])

@router.get("", response_model=SettingsPayload)
async def get_settings():
    settings = await translation_service.get_ai_settings()
    return SettingsPayload(**settings)

@router.post("")
async def save_settings(payload: SettingsPayload):
    await translation_service.save_ai_settings(payload.model_dump())
    return {"status": "success", "message": "Đã lưu cài đặt AI thành công"}

@router.get("/models")
async def fetch_models(base_url: str = None, api_key: str = None):
    try:
        models = await translation_service.fetch_available_models(api_base_url=base_url, api_key=api_key)
        return {"status": "success", "models": models}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Không thể lấy danh sách model: {str(e)}")

@router.post("/test")
async def test_ai_connection(payload: TestAiRequest):
    base_url = payload.api_base_url.rstrip("/")
    url = f"{base_url}/chat/completions"

    headers = {"Content-Type": "application/json"}
    if payload.api_key:
        headers["Authorization"] = f"Bearer {payload.api_key}"

    req_body = {
        "model": payload.model_name,
        "messages": [
            {"role": "system", "content": "Bạn là trợ lý dịch thuật."},
            {"role": "user", "content": payload.test_prompt or "你好，请回复：测试成功。"}
        ],
        "temperature": 0.2,
        "max_tokens": 50
    }

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(url, json=req_body, headers=headers)
            if resp.status_code != 200:
                return {
                    "status": "error",
                    "message": f"HTTP {resp.status_code}: {resp.text}"
                }
            res_json = resp.json()
            reply = res_json["choices"][0]["message"]["content"].strip()
            return {
                "status": "success",
                "message": "Kết nối thành công!",
                "response": reply
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Lỗi kết nối: {str(e)}"
        }

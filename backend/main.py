import os
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from sqlalchemy import select

from backend.config import BASE_DIR, DEFAULT_SYSTEM_PROMPT, DEFAULT_API_BASE_URL, DEFAULT_MODEL_NAME
from backend.database import engine, Base, AsyncSessionLocal, init_db
from backend.models import ScraperRule, AppSetting
from backend.scraper import DEFAULT_SCRAPER_RULES
from backend.translator import translation_service

from backend.routers import novels, chapters, glossary, settings, scraper_rules, discover, queue, auth
from backend.routers.auth import get_active_passcode

FRONTEND_DIR = BASE_DIR / "frontend"
STATIC_DIR = FRONTEND_DIR / "static"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Initialize DB tables
    await init_db()

    # 2. Seed initial scraper rules if table empty
    async with AsyncSessionLocal() as session:
        rule_check = await session.execute(select(ScraperRule))
        if not rule_check.scalars().first():
            for r_data in DEFAULT_SCRAPER_RULES:
                session.add(ScraperRule(**r_data))

        # Seed initial app settings
        setting_check = await session.execute(select(AppSetting))
        existing_keys = {s.key for s in setting_check.scalars().all()}
        defaults = {
            "ai_base_url": DEFAULT_API_BASE_URL,
            "ai_api_key": "",
            "ai_model_name": DEFAULT_MODEL_NAME,
            "ai_temperature": "0.3",
            "ai_system_prompt": DEFAULT_SYSTEM_PROMPT,
        }
        for k, v in defaults.items():
            if k not in existing_keys:
                session.add(AppSetting(key=k, value=v))

        await session.commit()

    # 3. Start background translation queue worker
    translation_service.start_background_worker()

    yield

    # Shutdown
    await translation_service.stop_background_worker()
    await engine.dispose()

app = FastAPI(
    title="AI Chinese Web Novel Reader & Translator",
    description="Hệ thống cào, dịch truyện Trung Quốc bằng AI & đọc đa nền tảng PC / Mobile PWA",
    version="1.0.0",
    lifespan=lifespan
)

# Auth Middleware for private single-user protection
class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Only protect /api/ routes, excluding /api/auth/
        if request.url.path.startswith("/api/") and not request.url.path.startswith("/api/auth/"):
            active_passcode = await get_active_passcode()
            if active_passcode:
                token = request.headers.get("X-App-Passcode") or request.headers.get("Authorization", "").replace("Bearer ", "").strip()
                if token != active_passcode:
                    return JSONResponse(
                        status_code=401,
                        content={"detail": "Unauthorized: Ứng dụng cá nhân yêu cầu mật khẩu truy cập"}
                    )
        return await call_next(request)

app.add_middleware(AuthMiddleware)

# CORS enabled for all origins (LAN access from mobile devices)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router)
app.include_router(novels.router)
app.include_router(chapters.router)
app.include_router(glossary.router)
app.include_router(settings.router)
app.include_router(scraper_rules.router)
app.include_router(discover.router)
app.include_router(queue.router)

# Mount static assets
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/manifest.json")
async def get_manifest():
    manifest_path = FRONTEND_DIR / "manifest.json"
    if manifest_path.exists():
        return FileResponse(manifest_path, media_type="application/manifest+json")
    return Response(content="{}", media_type="application/json")

@app.get("/sw.js")
async def get_service_worker():
    sw_path = FRONTEND_DIR / "sw.js"
    if sw_path.exists():
        return FileResponse(
            sw_path,
            media_type="application/javascript",
            headers={"Cache-Control": "no-cache, no-store, must-revalidate"}
        )
    return Response(content="", media_type="application/javascript")

@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    # If API or static, let it 404 naturally
    if full_path.startswith("api/") or full_path.startswith("static/"):
        return Response(status_code=404)
    # Serve index.html for all other routes
    index_path = FRONTEND_DIR / "index.html"
    if index_path.exists():
        return FileResponse(
            index_path,
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return Response(content="Frontend index.html not found", status_code=404)

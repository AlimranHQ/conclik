from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine

from app.routers import auth, profile
from app.routers.ai import router as ai_router
from app.routers.youtube import router as youtube_router
from app.routers.thumbnail import router as thumbnail_router
from app.routers.analysis import router as analysis_router
from app.routers.research import router as research_router
from app.routers.script import router as script_router
from app.routers.scene import router as scene_router

from app.seo_router import router as seo_router
from app.ai_services import ai_engine

# Database
Base.metadata.create_all(bind=engine)

# FastAPI Application
app = FastAPI(
    title="ContentPilot AI",
    version="3.6.0",
    description="Enterprise AI Content Operating System",
)

# Routers
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(ai_router)
app.include_router(seo_router)
app.include_router(youtube_router)
app.include_router(thumbnail_router)
app.include_router(analysis_router)
app.include_router(research_router)
app.include_router(script_router)
app.include_router(scene_router)


class ContentRequest(BaseModel):
    prompt: str
    category: str = "general"


@app.get("/")
def home():
    return {
        "app": "ContentPilot AI",
        "version": "3.6.0",
        "status": "Running Successfully",
        "developer": "AlimranHQ",
    }


@app.post("/generate")
def generate_content(request: ContentRequest):
    return ai_engine.generate_content(
        prompt=request.prompt,
        category=request.category,
    )


@app.get("/health")
def health():
    return {
        "status": "OK",
        "database": "Connected",
        "ai_engine": "Ready",
        "version": "3.6.0",
    }
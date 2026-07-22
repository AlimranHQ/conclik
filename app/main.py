from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine

from app.routers import auth, profile
from app.routers.ai import router as ai_router
from app.routers.youtube import router as youtube_router
from app.routers.thumbnail import router as thumbnail_router
from app.seo_router import router as seo_router

from app.ai_services import ai_engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ContentPilot AI",
    version="3.2.0",
    description="Production Ready Multi-AI Platform",
)


# Routers
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(ai_router)
app.include_router(seo_router)
app.include_router(youtube_router)
app.include_router(thumbnail_router)


class ContentRequest(BaseModel):
    prompt: str
    category: str = "general"


@app.get("/")
def home():
    return {
        "app": "ContentPilot AI",
        "version": "3.2.0",
        "status": "Running",
        "developer": "AlimranHQ",
    }


@app.post("/generate")
def generate(request: ContentRequest):
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
        "version": "3.2.0",
    }

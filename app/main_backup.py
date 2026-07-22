from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine
from app.routers import auth, profile
from app.routers.ai import router as ai_router
from app import seo_router
from app.ai_services import ai_engine


# Database
Base.metadata.create_all(bind=engine)


# FastAPI Application
app = FastAPI(
    title="ContentPilot AI",
    version="3.0.0",
    description="Production Ready Multi-AI Platform",
)


# Routers
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(ai_router)
app.include_router(seo_router.router)


# Request Schema
class ContentRequest(BaseModel):
    prompt: str
    category: str = "general"


# Home API
@app.get("/")
def home():
    return {
        "app": "ContentPilot AI",
        "version": "3.0.0",
        "status": "Running Successfully",
        "developer": "AlimranHQ",
    }


# Legacy AI Endpoint
@app.post("/generate")
def generate_content(request: ContentRequest):
    return ai_engine.generate_content(
        prompt=request.prompt,
        category=request.category,
    )


# Health Check
@app.get("/health")
def health():
    return {
        "status": "OK",
        "server": "ContentPilot AI Backend",
        "ai_engine": "Ready",
    }

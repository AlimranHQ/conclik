from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine
from app.routers import auth, profile
from app.ai_router import ai_router
from app.ai_services import ai_engine

# Database তৈরি
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title="ContentPilot AI",
    version="2.0.0",
    description="Multi-AI Content Generation Platform"
)

# Routers
app.include_router(auth.router)
app.include_router(profile.router)

# Request Model
class ContentRequest(BaseModel):
    prompt: str
    category: str = "general"


# Home Route
@app.get("/")
def home():
    return {
        "app": "ContentPilot AI",
        "version": "2.0.0",
        "status": "Running Successfully",
        "developer": "AlimranHQ"
    }


# AI Content Generator
@app.post("/generate")
def generate_content(request: ContentRequest):
    result = ai_engine.generate_content(
        prompt=request.prompt,
        category=request.category
    )
    return result


# Health Check
@app.get("/health")
def health():
    return {
        "status": "OK",
        "server": "ContentPilot AI Backend",
        "ai_engine": "Ready"
    }

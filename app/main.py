"""
Conclik Pilot AI
Version : 4.3.0
"""

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
from app.routers.director import router as director_router
from app.routers.orchestrator import router as orchestrator_router
from app.routers.project import router as project_router
from app.routers.workflow import router as workflow_router
from app.routers.memory import router as memory_router
from app.routers.decision import router as decision_router

from app.seo_router import router as seo_router
from app.ai_services import ai_engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Conclik Pilot AI",
    version="4.3.0",
    description="Enterprise AI Content Operating System",
)

# Core
app.include_router(auth.router)
app.include_router(profile.router)

# AI
app.include_router(ai_router)
app.include_router(seo_router)
app.include_router(youtube_router)
app.include_router(thumbnail_router)
app.include_router(analysis_router)
app.include_router(research_router)
app.include_router(script_router)
app.include_router(scene_router)

# Enterprise
app.include_router(director_router)
app.include_router(orchestrator_router)
app.include_router(project_router)
app.include_router(workflow_router)

# AI Brain
app.include_router(memory_router)
app.include_router(decision_router)


class ContentRequest(BaseModel):
    prompt: str
    category: str = "general"


@app.get("/")
def home():
    return {
        "brand": "Conclik",
        "product": "Conclik Pilot AI",
        "version": "4.3.0",
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
        "engine": "Ready",
        "version": "4.3.0",
    }

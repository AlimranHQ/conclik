"""
Conclik Pilot AI
Version : 5.0.0
"""

from fastapi import FastAPI

from app.database import Base, engine

from app.routers.auth import router as auth_router
from app.routers.profile import router as profile_router
from app.routers.ai import router as ai_router
from app.routers.analysis import router as analysis_router
from app.routers.content_studio import router as content_studio_router
from app.routers.decision import router as decision_router
from app.routers.director import router as director_router
from app.routers.gateway import router as gateway_router
from app.routers.gemini import router as gemini_router
from app.routers.gemini_connection import router as gemini_connection_router
from app.routers.gemini_generate import router as gemini_generate_router
from app.routers.image_prompt import router as image_prompt_router
from app.routers.memory import router as memory_router
from app.routers.orchestrator import router as orchestrator_router
from app.routers.pipeline import router as pipeline_router
from app.routers.plugin import router as plugin_router
from app.routers.plugin_executor import router as plugin_executor_router
from app.routers.project import router as project_router
from app.routers.research import router as research_router
from app.routers.scene import router as scene_router
from app.routers.script import router as script_router
from app.routers.thumbnail import router as thumbnail_router
from app.routers.workflow import router as workflow_router
from app.routers.youtube import router as youtube_router
from app.routers.agent_router import router as agent_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Conclik Pilot AI",
    version="5.0.0",
)

routers = [
    auth_router,
    profile_router,
    ai_router,
    analysis_router,
    content_studio_router,
    decision_router,
    director_router,
    gateway_router,
    gemini_router,
    gemini_connection_router,
    gemini_generate_router,
    image_prompt_router,
    memory_router,
    orchestrator_router,
    pipeline_router,
    plugin_router,
    plugin_executor_router,
    project_router,
    research_router,
    scene_router,
    script_router,
    thumbnail_router,
    workflow_router,
    youtube_router,
    agent_router,
]

for r in routers:
    app.include_router(r)

@app.get("/")
def home():
    return {
        "project": "Conclik Pilot AI",
        "version": "5.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

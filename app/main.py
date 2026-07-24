"""
Conclik Pilot AI
Version : 4.7.2
"""

from fastapi import FastAPI
from pydantic import BaseModel

from app.database import Base, engine

from app.routers import auth, profile
from app.routers.ai import router as ai_router
from app.routers.director import router as director_router
from app.routers.orchestrator import router as orchestrator_router
from app.routers.project import router as project_router
from app.routers.workflow import router as workflow_router
from app.routers.memory import router as memory_router
from app.routers.decision import router as decision_router
from app.routers.gateway import router as gateway_router
from app.routers.plugin import router as plugin_router
from app.routers.plugin_executor import router as plugin_executor_router
from app.routers.gemini import router as gemini_router
from app.routers.gemini_connection import router as gemini_connection_router
from app.routers.gemini_generate import router as gemini_generate_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Conclik Pilot AI",
    version="4.7.2",
    description="Enterprise AI Content Operating System",
)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(ai_router)

app.include_router(director_router)
app.include_router(orchestrator_router)
app.include_router(project_router)
app.include_router(workflow_router)

app.include_router(memory_router)
app.include_router(decision_router)

app.include_router(gateway_router)

app.include_router(plugin_router)
app.include_router(plugin_executor_router)

app.include_router(gemini_router)
app.include_router(gemini_connection_router)
app.include_router(gemini_generate_router)


class ContentRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "project": "Conclik Pilot AI",
        "version": "4.7.2",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "OK",
        "version": "4.7.2",
        "gateway": "Enabled",
        "gemini": "Integrated"
    }

from app.routers.agent_router import router as agent_router
try:
    app.include_router(agent_router)
except Exception as e:
    pass

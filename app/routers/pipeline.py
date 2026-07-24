"""
Conclik v5.0
Pipeline Router
"""

from fastapi import APIRouter
from app.pipeline.pipeline_manager import PipelineManager

router = APIRouter(
    prefix="/pipeline",
    tags=["Pipeline"],
)

manager = PipelineManager()


@router.get("/status")
def status():
    return {
        "status": "ready"
    }


@router.post("/run")
def run(task: dict):
    return manager.run(task)

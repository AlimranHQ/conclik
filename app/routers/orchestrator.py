"""
Conclik Pilot AI
Version : 5.2.0
Module  : Orchestrator Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.orchestrator import orchestrator

router = APIRouter(
    prefix="/orchestrator",
    tags=["Orchestrator"],
)


class ProjectRequest(BaseModel):
    prompt: str


@router.post("/create")
def create_project(request: ProjectRequest):
    return orchestrator.create_project(request.prompt)

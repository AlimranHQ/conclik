"""
Conclik Pilot AI
Version : 4.0.0
Module  : Orchestrator Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.orchestrator_service import orchestrator_service

router = APIRouter(
    prefix="/orchestrator",
    tags=["Orchestrator"],
)


class ProjectRequest(BaseModel):
    prompt: str


@router.post("/create")
def create_project(request: ProjectRequest):
    return orchestrator_service.create(request.prompt)

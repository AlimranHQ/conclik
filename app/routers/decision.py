"""
Conclik Pilot AI
Version : 4.3.0
Module : Decision Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.decision_service import decision_service

router = APIRouter(
    prefix="/decision",
    tags=["Decision"],
)


class DecisionRequest(BaseModel):
    prompt: str
    project: str = "default"


@router.post("/")
def decide(request: DecisionRequest):
    return decision_service.process(
        request.prompt,
        request.project,
    )

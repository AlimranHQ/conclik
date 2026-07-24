"""
Conclik Pilot AI
Version : 4.5.0
Module : Gateway Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_gateway_service import ai_gateway_service

router = APIRouter(
    prefix="/gateway",
    tags=["AI Gateway"],
)


class GatewayRequest(BaseModel):
    prompt: str


@router.post("/")
def generate(request: GatewayRequest):

    return ai_gateway_service.generate(
        request.prompt
    )

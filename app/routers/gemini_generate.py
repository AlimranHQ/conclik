"""
Conclik Pilot AI
Version : 4.7.2
Module : Gemini Generate Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_generate_service import (
    gemini_generate_service,
)

router = APIRouter(
    prefix="/gemini-generate",
    tags=["Gemini Generate"],
)


class Prompt(BaseModel):
    prompt: str


@router.post("/")
def generate(data: Prompt):

    return {
        "response": gemini_generate_service.generate(
            data.prompt
        )
    }

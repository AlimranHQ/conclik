"""
Conclik Pilot AI
Version : 4.7.0
Module : Gemini Router
"""

from fastapi import APIRouter

from app.services.gemini_service import gemini_service

router = APIRouter(
    prefix="/gemini",
    tags=["Gemini"],
)


@router.get("/status")
def status():
    return gemini_service.status()

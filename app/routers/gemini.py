"""
Conclik Pilot AI
Version : 5.2.0
Module : Gemini Router
"""

from fastapi import APIRouter
from app.providers.gemini_client import gemini_client

router = APIRouter(
    prefix="/gemini",
    tags=["Gemini"],
)


@router.get("/status")
def status():
    return gemini_client.info()

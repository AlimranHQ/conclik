"""
Conclik Pilot AI
Version : 4.7.1
Module : Gemini Connection Router
"""

from fastapi import APIRouter

from app.services.gemini_connection_service import (
    gemini_connection_service,
)

router = APIRouter(
    prefix="/gemini-connection",
    tags=["Gemini Connection"],
)


@router.get("/")
def status():

    return gemini_connection_service.status()

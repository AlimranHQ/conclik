"""
Conclik Pilot AI
Version : 5.2.0
Module : Gemini Connection Router
"""

from fastapi import APIRouter
from app.providers.gemini_connection import gemini_connection

router = APIRouter(
    prefix="/gemini-connection",
    tags=["Gemini Connection"],
)


@router.get("/")
def status():
    return gemini_connection.connect()

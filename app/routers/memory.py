"""
Conclik Pilot AI
Version : 4.3.0
Module : Memory Router
"""

from fastapi import APIRouter

from app.services.memory_service import memory_service

router = APIRouter(
    prefix="/memory",
    tags=["Memory"],
)


@router.get("/{key}")
def get_memory(key: str):
    return {
        "key": key,
        "value": memory_service.load(key),
    }


@router.delete("/clear")
def clear_memory():
    memory_service.clear()
    return {
        "success": True,
        "message": "Memory cleared",
    }

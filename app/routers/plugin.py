"""
Conclik Pilot AI
Version : 4.6.0
Module : Plugin Router
"""

from fastapi import APIRouter

from app.services.plugin_service import plugin_service

router = APIRouter(
    prefix="/plugins",
    tags=["Plugins"],
)


@router.get("/")
def list_plugins():
    return {
        "plugins": plugin_service.plugins()
    }

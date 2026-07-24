"""
Conclik Pilot AI
Version : 4.6.1
Module : Plugin Executor Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.plugin_executor_service import plugin_executor_service

router = APIRouter(
    prefix="/plugin-executor",
    tags=["Plugin Executor"],
)


class PluginRequest(BaseModel):
    plugin: str


@router.post("/")
def execute(request: PluginRequest):

    return plugin_executor_service.execute(
        request.plugin
    )

"""
Conclik Pilot AI
Version : 5.0.0
Module : Content Studio Router
"""

from fastapi import APIRouter

from app.schemas.content_studio_schema import (
    ContentStudioRequest,
)

from app.services.content_studio_service import (
    content_studio_service,
)

router = APIRouter(
    prefix="/content-studio",
    tags=["Content Studio"],
)


@router.post("/")
def generate(data: ContentStudioRequest):

    return {
        "result": content_studio_service.generate(
            data.topic
        )
    }

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.youtube_service import youtube_service

router = APIRouter(
    prefix="/youtube",
    tags=["YouTube AI"]
)


class YouTubeRequest(BaseModel):
    topic: str


@router.post("/generate")
def generate(request: YouTubeRequest):
    return youtube_service.generate(
        topic=request.topic
    )

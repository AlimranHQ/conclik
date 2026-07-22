from fastapi import APIRouter
from pydantic import BaseModel

from app.services.thumbnail_service import thumbnail_service

router = APIRouter(
    prefix="/thumbnail",
    tags=["Thumbnail AI"],
)


class ThumbnailRequest(BaseModel):
    topic: str


@router.post("/generate")
def generate(request: ThumbnailRequest):
    return thumbnail_service.generate(
        topic=request.topic
    )

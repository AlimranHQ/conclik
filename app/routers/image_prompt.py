from fastapi import APIRouter
from pydantic import BaseModel

from app.services.image_prompt_service import image_prompt_service

router = APIRouter(
    prefix="/image-prompt",
    tags=["Image Prompt AI"]
)


class ImagePromptRequest(BaseModel):
    topic: str
    scene_title: str
    style: str = "cinematic"


@router.post("/generate")
def generate_image_prompt(request: ImagePromptRequest):
    return image_prompt_service.generate(
        topic=request.topic,
        scene_title=request.scene_title,
        style=request.style,
    )

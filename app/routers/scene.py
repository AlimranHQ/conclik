from fastapi import APIRouter
from pydantic import BaseModel

from app.services.scene_service import scene_service

router = APIRouter(
    prefix="/scene",
    tags=["Scene AI"]
)


class SceneRequest(BaseModel):
    topic: str
    duration: int = 10


@router.post("/generate")
def generate_scene(request: SceneRequest):

    return scene_service.generate(
        topic=request.topic,
        duration=request.duration,
    )

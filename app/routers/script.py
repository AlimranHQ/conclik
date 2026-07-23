from fastapi import APIRouter
from pydantic import BaseModel

from app.services.script_service import script_service

router = APIRouter(
    prefix="/script",
    tags=["Script AI"]
)


class ScriptRequest(BaseModel):
    topic: str
    duration: int = 10
    language: str = "English"


@router.post("/generate")
def generate_script(request: ScriptRequest):

    return script_service.generate(
        topic=request.topic,
        duration=request.duration,
        language=request.language,
    )

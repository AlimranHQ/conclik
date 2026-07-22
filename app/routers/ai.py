from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import ai_service

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


class AIRequest(BaseModel):
    prompt: str
    category: str = "general"
    provider: str = "auto"


@router.post("/generate")
def generate(request: AIRequest):
    return ai_service.generate(
        prompt=request.prompt,
        category=request.category,
        provider=request.provider,
    )

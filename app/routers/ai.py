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


@router.post("/generate")
async def generate(request: AIRequest):

    return await ai_service.generate(
        prompt=request.prompt,
        category=request.category,
    )

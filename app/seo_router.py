from fastapi import APIRouter
from pydantic import BaseModel

from app.seo_service import seo_service

router = APIRouter(
    prefix="/seo",
    tags=["SEO"]
)


class SEORequest(BaseModel):
    topic: str
    language: str = "English"


@router.post("/generate")
def generate_seo(request: SEORequest):

    return seo_service.generate(
        topic=request.topic,
        language=request.language
    )

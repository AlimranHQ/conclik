from fastapi import APIRouter
from pydantic import BaseModel

from app.services.research_service import research_service

router = APIRouter(
    prefix="/research",
    tags=["Research AI"]
)


class ResearchRequest(BaseModel):
    topic: str
    language: str = "English"


@router.post("/run")
def run_research(request: ResearchRequest):

    return research_service.research(
        topic=request.topic,
        language=request.language,
    )

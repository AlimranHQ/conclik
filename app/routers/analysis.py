from fastapi import APIRouter
from pydantic import BaseModel

from app.services.analysis_service import analysis_service

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis AI"],
)


class AnalysisRequest(BaseModel):
    topic: str
    duration: int = 10


@router.post("/run")
def run_analysis(request: AnalysisRequest):
    return analysis_service.analyze(
        topic=request.topic,
        duration=request.duration,
    )

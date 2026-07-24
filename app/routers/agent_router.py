"""
Conclik Pilot AI - Agent Router
Version: 5.0.0
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.pipeline_service import pipeline_service

router = APIRouter(prefix="/agents", tags=["Multi-Agent Pipeline"])

class PipelineRequest(BaseModel):
    topic: str

@router.post("/run-pipeline")
async def run_pipeline(request: PipelineRequest):
    try:
        result = await pipeline_service.run_pipeline(request.topic)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

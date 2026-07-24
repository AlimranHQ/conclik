from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.orchestrator import MultiAgentOrchestrator

router = APIRouter(prefix="/agents", tags=["Multi-Agent System"])
orchestrator = MultiAgentOrchestrator()

class TopicRequest(BaseModel):
    topic: str
    tone: str = "Engaging"

@router.post("/run-pipeline")
async def run_multi_agent_pipeline(request: TopicRequest):
    """
    Executes the complete v5.0 Multi-Agent Pipeline (Research to QA).
    """
    try:
        result = await orchestrator.run_pipeline(topic=request.topic, tone=request.tone)
        if result.get("status") == "error":
            raise HTTPException(status_code=500, detail=result.get("message"))
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

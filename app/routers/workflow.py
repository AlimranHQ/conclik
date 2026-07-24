"""
Conclik Pilot AI
Version : 4.2.0
Module  : Workflow Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.workflow_service import workflow_service


router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)


class WorkflowRequest(BaseModel):
    job: str


@router.post("/create")
def create(request: WorkflowRequest):

    workflow_service.create(request.job)

    return {
        "success": True,
        "queued": request.job
    }


@router.post("/run")
def run():

    return workflow_service.run()

"""
Conclik Pilot AI
Version : 4.1.0
Module  : Project Schema
"""

from datetime import datetime
from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    prompt: str


class ProjectResponse(BaseModel):
    id: int
    title: str
    prompt: str
    status: str
    workflow: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True

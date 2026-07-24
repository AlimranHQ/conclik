"""
Conclik Pilot AI
Version : 5.0.0
Module : Content Studio Schema
"""

from pydantic import BaseModel


class ContentStudioRequest(BaseModel):
    topic: str
    platform: str = "youtube"

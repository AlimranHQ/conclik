"""
Conclik v5.1
Director Router
"""

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.director import director

router = APIRouter(
    prefix="/director",
    tags=["Director"],
)


class Prompt(BaseModel):
    prompt: str


@router.post("/")
def execute(data: Prompt):

    return director.execute(data.prompt)

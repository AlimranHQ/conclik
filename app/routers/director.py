from fastapi import APIRouter
from app.core.director import director

router = APIRouter(
    prefix="/director",
    tags=["Director"],
)


@router.post("/workflow")
def build_workflow():
    return director.build()

"""
Conclik Pilot AI
Version : 4.1.0
Module  : Project Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.project_schema import ProjectCreate
from app.services.project_service import project_service


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
):
    return project_service.create(db, data)


@router.get("/")
def list_projects(
    db: Session = Depends(get_db),
):
    return project_service.get_all(db)


@router.get("/{project_id}")
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = project_service.get(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return project


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    result = project_service.delete(db, project_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return {
        "success": True,
        "message": "Project deleted",
    }


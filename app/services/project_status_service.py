"""
Conclik Pilot AI
Version : 4.1.0
Module  : Project Status Service
"""

from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectStatusService:

    def update_status(
        self,
        db: Session,
        project_id: int,
        status: str,
    ):

        project = (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

        if not project:
            return None

        project.status = status

        db.commit()
        db.refresh(project)

        return project


project_status_service = ProjectStatusService()

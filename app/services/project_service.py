"""
Conclik Pilot AI
Version : 4.1.0
Module  : Project Service
"""

from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project_schema import ProjectCreate


class ProjectService:

    def create(self, db: Session, data: ProjectCreate):

        project = Project(
            title=data.title,
            prompt=data.prompt,
            status="pending",
            workflow="initialized",
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    def get_all(self, db: Session):

        return (
            db.query(Project)
            .order_by(Project.id.desc())
            .all()
        )

    def get(self, db: Session, project_id: int):

        return (
            db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def delete(self, db: Session, project_id: int):

        project = self.get(db, project_id)

        if not project:
            return None

        db.delete(project)
        db.commit()

        return True


project_service = ProjectService()

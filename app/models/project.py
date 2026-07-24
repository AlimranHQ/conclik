"""
Conclik Pilot AI
Version : 4.1.0
Module  : Project Model
"""

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    prompt = Column(Text, nullable=False)

    status = Column(String(50), default="pending")

    workflow = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

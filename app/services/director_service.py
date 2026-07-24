"""
Conclik Pilot AI
Version : 4.0.0
Module  : Director Service
"""

from app.core.director import director


class DirectorService:

    def create_workflow(self):
        return director.build()


director_service = DirectorService()

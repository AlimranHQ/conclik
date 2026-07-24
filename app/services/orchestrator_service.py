"""
Conclik Pilot AI
Version : 4.0.0
Module  : Orchestrator Service
"""

from app.core.orchestrator import orchestrator


class OrchestratorService:

    def create(self, prompt: str):
        return orchestrator.create_project(prompt)


orchestrator_service = OrchestratorService()

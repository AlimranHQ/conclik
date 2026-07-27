"""
Conclik Pilot AI
Version : 5.2.0
Module  : AI Orchestrator
"""

from app.core.director import director


class AIOrchestrator:

    def create_project(self, prompt: str):

        workflow = director.execute(prompt)

        return {
            "success": True,
            "project": prompt,
            "workflow": workflow,
            "status": "Project Initialized"
        }


orchestrator = AIOrchestrator()

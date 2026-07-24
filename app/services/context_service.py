"""
Conclik Pilot AI
Version : 4.3.0
Module : Context Service
"""

from app.core.context_engine import context_engine


class ContextService:

    def build(self, prompt: str, project: str = "default"):
        return context_engine.build_context(prompt, project)


context_service = ContextService()

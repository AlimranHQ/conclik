"""
Conclik Pilot AI
Version : 4.3.0
Module : Decision Service
"""

from app.core.decision_engine import decision_engine


class DecisionService:

    def process(self, prompt: str, project: str = "default"):
        return decision_engine.decide(prompt, project)


decision_service = DecisionService()

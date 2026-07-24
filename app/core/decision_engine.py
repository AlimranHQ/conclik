"""
Conclik Pilot AI
Version : 4.3.0
Module  : Decision Engine
"""

from app.core.prompt_optimizer import prompt_optimizer


class DecisionEngine:

    def decide(
        self,
        prompt: str,
        project: str = "default",
    ):

        optimized = prompt_optimizer.optimize(
            prompt,
            project,
        )

        return {
            "provider": "auto",
            "optimized": optimized,
            "status": "ready",
        }


decision_engine = DecisionEngine()

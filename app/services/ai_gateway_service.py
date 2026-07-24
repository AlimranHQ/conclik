"""
Conclik Pilot AI
Version : 4.5.0
Module : AI Gateway Service
"""

from app.core.ai_gateway import ai_gateway


class AIGatewayService:

    def generate(self, prompt):

        return ai_gateway.generate(prompt)


ai_gateway_service = AIGatewayService()

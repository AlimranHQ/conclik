"""
Conclik Pilot AI
Version : 4.5.0
Module : AI Gateway
"""

from app.core.request_validator import request_validator
from app.core.response_formatter import response_formatter

from app.services.provider_router_service import provider_router_service


class AIGateway:

    def generate(self, prompt: str):

        if not request_validator.validate(prompt):

            return response_formatter.error(
                "Invalid Prompt"
            )

        result = provider_router_service.generate(prompt)

        return response_formatter.success(
            result["provider"],
            result,
        )


ai_gateway = AIGateway()

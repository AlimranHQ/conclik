"""
Conclik Pilot AI
Version : 4.4.0
Module : Provider Router Service
"""

from app.core.failover_engine import failover_engine
from app.services.provider_service import provider_service


class ProviderRouterService:

    def generate(self, prompt: str):

        provider = failover_engine.provider()

        return provider_service.generate(
            prompt,
            provider,
        )


provider_router_service = ProviderRouterService()

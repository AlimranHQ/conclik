"""
Conclik Pilot AI
Version : 4.4.0
Module : Provider Service
"""

from app.providers.provider_factory import provider_factory


class ProviderService:

    def generate(
        self,
        prompt,
        provider="gemini",
    ):

        engine = provider_factory.get(provider)

        return engine.generate(prompt)


provider_service = ProviderService()

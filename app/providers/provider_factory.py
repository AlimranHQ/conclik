"""
Conclik Pilot AI
Version : 4.4.0
Module : Provider Factory
"""

from app.providers.gemini_provider import gemini_provider
from app.providers.openai_provider import openai_provider


class ProviderFactory:

    def get(self, provider="gemini"):

        if provider.lower() == "openai":
            return openai_provider

        return gemini_provider


provider_factory = ProviderFactory()

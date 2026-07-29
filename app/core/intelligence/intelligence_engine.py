"""
Conclik Pilot AI
Intelligence Engine
Version : 1.0.0
"""

from app.core.intelligence.provider_selector import provider_selector
from app.core.providers.provider_manager import provider_manager


class IntelligenceEngine:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
        preferred_provider: str = "gemini",
        **kwargs,
    ):

        provider = provider_selector.select(preferred_provider)

        if provider is None:
            raise RuntimeError("No AI provider available.")

        return await provider_manager.generate(
            provider_name=provider.name,
            prompt=prompt,
            category=category,
            **kwargs,
        )

    async def health(
        self,
        preferred_provider: str = "gemini",
    ):

        provider = provider_selector.select(preferred_provider)

        if provider is None:
            return False

        return await provider_manager.health(provider.name)


intelligence_engine = IntelligenceEngine()


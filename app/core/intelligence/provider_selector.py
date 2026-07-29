"""
Conclik Pilot AI
Provider Selector
Version : 1.0.0
"""

from app.core.providers.provider_registry import provider_registry


class ProviderSelector:

    def select(
        self,
        preferred: str = "gemini",
    ):

        provider = provider_registry.get(preferred)

        if provider:
            return provider

        providers = provider_registry.all()

        if providers:
            return providers[0]

        return None


provider_selector = ProviderSelector()


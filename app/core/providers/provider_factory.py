"""
Conclik Pilot AI
Provider Factory
Version : 1.0.0
"""

from app.core.providers.provider_registry import provider_registry


class ProviderFactory:

    def create(
        self,
        provider_name: str,
    ):

        return provider_registry.get(provider_name)


provider_factory = ProviderFactory()


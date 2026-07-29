"""
Conclik Pilot AI
Provider Registry
Version : 1.0.0
"""

from typing import Dict

from app.core.providers.base_provider import BaseProvider


class ProviderRegistry:

    def __init__(self):
        self._providers: Dict[str, BaseProvider] = {}

    def register(
        self,
        provider: BaseProvider,
    ) -> None:

        self._providers[provider.name] = provider

    def get(
        self,
        name: str,
    ) -> BaseProvider | None:

        return self._providers.get(name)

    def all(self):

        return list(self._providers.values())


provider_registry = ProviderRegistry()


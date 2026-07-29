"""
Conclik Pilot AI
Provider Manager
Version : 2.0.0
"""

from app.core.providers.provider_factory import provider_factory


class ProviderManager:

    async def generate(
        self,
        provider_name: str,
        prompt: str,
        category: str = "general",
        **kwargs,
    ) -> str:

        provider = provider_factory.create(provider_name)

        if provider is None:
            raise ValueError(
                f"Provider '{provider_name}' not found."
            )

        return await provider.generate(
            prompt=prompt,
            category=category,
            **kwargs,
        )

    async def health(
        self,
        provider_name: str,
    ) -> bool:

        provider = provider_factory.create(provider_name)

        if provider is None:
            return False

        return await provider.health()


provider_manager = ProviderManager()


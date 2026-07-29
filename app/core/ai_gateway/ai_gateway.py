from app.core.ai_gateway.provider_selector import provider_selector
from app.core.providers.provider_manager import provider_manager

class AIGateway:

    async def generate(
        self,
        prompt,
        provider=None,
        category="general",
        **kwargs,
    ):
        provider_name = provider_selector.select(provider)

        return await provider_manager.generate(
            provider_name,
            prompt,
            category=category,
            **kwargs,
        )

ai_gateway = AIGateway()

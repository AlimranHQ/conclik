"""
Conclik Pilot AI
Gemini Provider Adapter
Version : 2.0.0
"""

from app.core.providers.base_provider import BaseProvider
from app.providers.gemini_client import gemini_client


class GeminiProvider(BaseProvider):

    @property
    def name(self) -> str:
        return "gemini"

    async def generate(
        self,
        prompt: str,
        category: str = "general",
        **kwargs,
    ) -> str:

        return await gemini_client.generate_content(
            prompt=prompt,
            category=category,
        )

    async def health(self) -> bool:
        return True


gemini_provider = GeminiProvider()


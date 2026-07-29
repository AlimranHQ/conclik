"""
Conclik Pilot AI
Gemini Provider Adapter
Version : 3.0.0
"""

from app.core.providers.base_provider import BaseProvider
from app.core.providers.loaders.gemini_loader import load_gemini


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

        gemini = load_gemini()

        return await gemini.generate_content(
            prompt=prompt,
            category=category,
        )

    async def health(self) -> bool:
        return True


gemini_provider = GeminiProvider()


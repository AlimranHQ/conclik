"""
Conclik Pilot AI
Universal Generate Service
Version : 7.0.0
"""

from app.core.intelligence.intelligence_engine import intelligence_engine


class GenerateService:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
    ):

        return await intelligence_engine.generate(
            prompt=prompt,
            category=category,
            preferred_provider="gemini",
        )


generate_service = GenerateService()


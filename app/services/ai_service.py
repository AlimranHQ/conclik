"""
Conclik Pilot AI
Version : 5.2.0
AI Service
"""

from app.providers.gemini_client import gemini_client


class AIService:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
    ):
        return await gemini_client.generate_content(
            prompt=prompt,
            category=category,
        )


ai_service = AIService()

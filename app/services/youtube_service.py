"""
Conclik Pilot AI
YouTube Service
Version : 7.0.0
Architecture : Intelligence Engine
"""

from app.core.intelligence.intelligence_engine import intelligence_engine


class YouTubeService:

    async def generate(
        self,
        prompt: str,
        category: str = "youtube",
    ):

        return await intelligence_engine.generate(
            prompt=prompt,
            category=category,
            preferred_provider="gemini",
        )


youtube_service = YouTubeService()


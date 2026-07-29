"""
Conclik Pilot AI
Thumbnail Service
Version : 7.0.0
Architecture : Intelligence Engine
"""

from app.prompts.thumbnail_prompt import thumbnail_prompt
from app.core.intelligence.intelligence_engine import intelligence_engine


class ThumbnailService:

    async def generate(self, topic: str):

        prompt = thumbnail_prompt(topic)

        return await intelligence_engine.generate(
            prompt=prompt,
            category="thumbnail",
            preferred_provider="gemini",
        )


thumbnail_service = ThumbnailService()


"""
Conclik Pilot AI
Thumbnail Service
"""

from app.prompts.thumbnail_prompt import thumbnail_prompt
from app.providers.gemini_client import gemini_client


class ThumbnailService:

    async def generate(self, topic: str):

        prompt = thumbnail_prompt(topic)

        return await gemini_client.generate_content(
            prompt=prompt,
            category="thumbnail",
        )


thumbnail_service = ThumbnailService()

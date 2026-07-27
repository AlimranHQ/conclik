"""
Conclik Pilot AI
YouTube Service
"""

from app.prompts.youtube_prompt import youtube_prompt
from app.providers.gemini_client import gemini_client


class YouTubeService:

    async def generate(self, topic: str):

        prompt = youtube_prompt(topic)

        return await gemini_client.generate_content(
            prompt=prompt,
            category="youtube",
        )


youtube_service = YouTubeService()

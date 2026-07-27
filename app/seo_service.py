"""
Conclik Pilot AI
SEO Service
"""

from app.providers.gemini_client import gemini_client
from app.prompts.seo_prompt import YOUTUBE_SEO_PROMPT


class SEOService:

    async def generate(
        self,
        topic: str,
        language: str = "English",
    ):

        prompt = YOUTUBE_SEO_PROMPT.format(
            topic=topic,
            language=language,
        )

        return await gemini_client.generate_content(
            prompt=prompt,
            category="seo",
        )


seo_service = SEOService()

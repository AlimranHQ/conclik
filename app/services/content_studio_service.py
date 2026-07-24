"""
Conclik Pilot AI
Version : 5.0.0
Module : Content Studio Service
"""

from app.services.gemini_generate_service import (
    gemini_generate_service,
)


class ContentStudioService:

    def generate(self, topic: str):

        prompt = f"""
Create:

1. YouTube Title
2. SEO Description
3. 15 Hashtags
4. Thumbnail Prompt
5. Facebook Caption
6. Instagram Caption

Topic:

{topic}
"""

        return gemini_generate_service.generate(prompt)


content_studio_service = ContentStudioService()

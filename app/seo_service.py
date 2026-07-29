"""
Conclik Pilot AI
SEO Service
Version : 7.0.0
Architecture : Intelligence Engine
"""

from app.core.intelligence.intelligence_engine import intelligence_engine


class SEOService:

    async def generate(
        self,
        prompt: str,
    ):

        return await intelligence_engine.generate(
            prompt=prompt,
            category="seo",
            preferred_provider="gemini",
        )


seo_service = SEOService()


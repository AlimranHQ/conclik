"""
Conclik Pilot AI
Version : 7.0.0
Module : AI Service
Architecture : Intelligence Engine
"""

from app.core.intelligence.intelligence_engine import intelligence_engine
from app.security.security_manager import security_manager


class AIService:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
        provider: str = "gemini",
        **kwargs,
    ):

        if not security_manager.secure(
            prompt=prompt,
            role="user",
            action=category,
            identifier="anonymous",
        ):
            return {
                "success": False,
                "error": "Security validation failed",
            }

        return await intelligence_engine.generate(
            prompt=prompt,
            category=category,
            preferred_provider=provider,
            **kwargs,
        )


ai_service = AIService()


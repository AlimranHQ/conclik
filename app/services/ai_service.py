"""
Conclik Pilot AI
Version : 5.4.0
Module : AI Service
"""

from app.providers.gemini_client import gemini_client
from app.security.security_manager import security_manager


class AIService:

    async def generate(
        self,
        prompt: str,
        category: str = "general",
        provider: str = "auto",
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

        return await gemini_client.generate_content(
            prompt=prompt,
            category=category,
        )


ai_service = AIService()

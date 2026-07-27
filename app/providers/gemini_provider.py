"""
Conclik Pilot AI
Version : 5.2.0
Unified Gemini Provider
"""

from app.providers.base_provider import BaseProvider
from app.providers.gemini_client import gemini_client


class GeminiProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Gemini",
            "content": gemini_client.generate(prompt),
            "status": "success",
        }


gemini_provider = GeminiProvider()

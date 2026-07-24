"""
Conclik Pilot AI
Version : 4.4.0
Module : Gemini Provider
"""

from app.providers.base_provider import BaseProvider


class GeminiProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Gemini",
            "prompt": prompt,
            "status": "ready"
        }


gemini_provider = GeminiProvider()

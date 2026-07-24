"""
Conclik Pilot AI
Version : 4.7.2
Module : Gemini Generate Service
"""

from app.providers.gemini_generate import (
    gemini_generate,
)


class GeminiGenerateService:

    def generate(
        self,
        prompt: str,
    ):

        return gemini_generate.generate(prompt)


gemini_generate_service = GeminiGenerateService()

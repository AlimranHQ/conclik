"""
Conclik Pilot AI
Version : 5.2.0
Unified Gemini Generate Service
"""

from app.providers.gemini_client import gemini_client


class GeminiGenerateService:

    def generate(self, prompt: str):
        return gemini_client.generate(prompt)


gemini_generate_service = GeminiGenerateService()

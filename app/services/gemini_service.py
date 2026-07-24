"""
Conclik Pilot AI
Version : 4.7.0
Module : Gemini Service
"""

from app.providers.gemini_client import gemini_client


class GeminiService:

    def status(self):
        return gemini_client.info()


gemini_service = GeminiService()

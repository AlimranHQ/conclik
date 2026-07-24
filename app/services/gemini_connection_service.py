"""
Conclik Pilot AI
Version : 4.7.1
Module : Gemini Connection Service
"""

from app.providers.gemini_connection import gemini_connection


class GeminiConnectionService:

    def status(self):

        return gemini_connection.connect()


gemini_connection_service = GeminiConnectionService()

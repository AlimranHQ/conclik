"""
Conclik Pilot AI
Version : 4.7.0
Module : Gemini Client
"""

from app.core.api_keys import api_keys
from app.core.model_selector import model_selector


class GeminiClient:

    def info(self):

        return {
            "provider": "Gemini",
            "model": model_selector.gemini(),
            "api_key_loaded": bool(api_keys.gemini),
        }


gemini_client = GeminiClient()

"""
Conclik Pilot AI
Version : 4.7.1
Module : Gemini Config
"""

from app.core.api_keys import api_keys
from app.core.model_selector import model_selector


class GeminiConfig:

    def config(self):

        return {
            "api_key": api_keys.gemini,
            "model": model_selector.gemini(),
        }


gemini_config = GeminiConfig()

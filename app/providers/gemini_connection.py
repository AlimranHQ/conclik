"""
Conclik Pilot AI
Version : 4.7.1
Module : Gemini Connection
"""

from app.core.gemini_config import gemini_config


class GeminiConnection:

    def connect(self):

        cfg = gemini_config.config()

        return {
            "connected": bool(cfg["api_key"]),
            "model": cfg["model"],
        }


gemini_connection = GeminiConnection()

"""
Conclik Pilot AI
Version : 4.7.0
Module : API Keys
"""

import os


class APIKeys:

    @property
    def gemini(self):
        return os.getenv("GEMINI_API_KEY", "")


api_keys = APIKeys()

"""
Conclik Pilot AI
Version : 4.7.2
Module : Gemini SDK
"""

from google import genai

from app.core.api_keys import api_keys


class GeminiSDK:

    def client(self):
        return genai.Client(
            api_key=api_keys.gemini
        )


gemini_sdk = GeminiSDK()

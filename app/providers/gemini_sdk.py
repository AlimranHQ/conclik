"""
Conclik Pilot AI
Version : 4.7.2
Module : Gemini SDK
"""

import google.generativeai as genai

from app.core.api_keys import api_keys


class GeminiSDK:

    def client(self):
        genai.configure(api_key=api_keys.gemini)
        return genai


gemini_sdk = GeminiSDK()

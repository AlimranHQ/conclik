"""
Conclik Pilot AI
Version : 5.2.0
Unified Gemini Client
"""

import google.generativeai as genai

from app.core.api_keys import api_keys
from app.core.model_selector import model_selector

if api_keys.gemini:
    genai.configure(api_key=api_keys.gemini)


class GeminiClient:

    def __init__(self):
        self.model_name = model_selector.gemini()
        self.model = genai.GenerativeModel(self.model_name)

    async def generate_content(
        self,
        prompt: str,
        category: str = "general",
        system_instruction: str | None = None,
    ):

        if system_instruction:
            prompt = f"{system_instruction}\n\n{prompt}"

        response = self.model.generate_content(prompt)

        return {
            "success": True,
            "provider": "Gemini",
            "category": category,
            "content": response.text,
        }

    def info(self):
        return {
            "provider": "Gemini",
            "model": self.model_name,
            "api_key_loaded": bool(api_keys.gemini),
        }


gemini_client = GeminiClient()

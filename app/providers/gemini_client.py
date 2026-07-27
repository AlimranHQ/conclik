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
        self.model = genai.GenerativeModel(
            model_selector.gemini()
        )

    def generate(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text

    async def generate_content(
        self,
        prompt: str,
        system_instruction: str = None,
    ):

        full_prompt = (
            f"System Instruction: {system_instruction}\n\nPrompt: {prompt}"
            if system_instruction
            else prompt
        )

        return self.generate(full_prompt)

    def info(self):
        return {
            "provider": "Gemini",
            "model": model_selector.gemini(),
            "api_key_loaded": bool(api_keys.gemini),
        }


gemini_client = GeminiClient()

"""
Conclik Pilot AI
Version : 4.7.0
Module : Gemini Client
"""

import google.generativeai as genai
from app.core.api_keys import api_keys
from app.core.model_selector import model_selector

# Configure Gemini API Key
if api_keys.gemini:
    genai.configure(api_key=api_keys.gemini)

class GeminiClient:
    def __init__(self):
        self.model_name = model_selector.gemini()

    async def generate_content(self, prompt: str, system_instruction: str = None) -> str:
        """
        Generates content using Google Gemini API.
        """
        try:
            full_prompt = f"System Instruction: {system_instruction}\n\nPrompt: {prompt}" if system_instruction else prompt
            
            model = genai.GenerativeModel(self.model_name)
            response = model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API Error: {str(e)}")

    def info(self):
        return {
            "provider": "Gemini",
            "model": self.model_name,
            "api_key_loaded": bool(api_keys.gemini),
        }

gemini_client = GeminiClient()

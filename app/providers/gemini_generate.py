"""
Conclik Pilot AI
Version : 4.8.1
Official Gemini SDK
Production Ready
"""

import os

from dotenv import load_dotenv
from google import genai

from app.core.model_selector import model_selector

load_dotenv()


class GeminiGenerate:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate(self, prompt: str):

        try:
            response = self.client.models.generate_content(
                model=model_selector.gemini(),
                contents=prompt,
            )

            return response.text

        except Exception:
            response = self.client.models.generate_content(
                model=model_selector.fallback(),
                contents=prompt,
            )

            return response.text


gemini_generate = GeminiGenerate()

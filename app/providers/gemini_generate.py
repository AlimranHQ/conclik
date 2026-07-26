"""
Conclik Pilot AI
Version : 4.8.1
Gemini Generate Provider
"""

import os

import google.generativeai as genai
from dotenv import load_dotenv

from app.core.model_selector import model_selector

load_dotenv()


class GeminiGenerate:

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(model_selector.gemini())

    def generate(self, prompt: str):

        try:
            response = self.model.generate_content(prompt)
            return response.text

        except Exception:
            fallback = genai.GenerativeModel(model_selector.fallback())
            response = fallback.generate_content(prompt)
            return response.text


gemini_generate = GeminiGenerate()

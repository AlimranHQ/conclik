"""
Conclik Pilot AI
Version : 4.4.0
Module : OpenAI Provider
"""

from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "OpenAI",
            "prompt": prompt,
            "status": "ready"
        }


openai_provider = OpenAIProvider()

"""
Conclik Pilot AI
Version : 4.4.0
Module : Ollama Provider
"""

from app.providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Ollama",
            "prompt": prompt,
            "status": "ready"
        }


ollama_provider = OllamaProvider()

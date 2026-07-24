"""
Conclik Pilot AI
Version : 4.4.0
Module : Mistral Provider
"""

from app.providers.base_provider import BaseProvider


class MistralProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Mistral",
            "prompt": prompt,
            "status": "ready"
        }


mistral_provider = MistralProvider()

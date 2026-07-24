"""
Conclik Pilot AI
Version : 4.4.0
Module : Grok Provider
"""

from app.providers.base_provider import BaseProvider


class GrokProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "Grok",
            "prompt": prompt,
            "status": "ready"
        }


grok_provider = GrokProvider()

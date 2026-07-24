"""
Conclik Pilot AI
Version : 4.4.0
Module : DeepSeek Provider
"""

from app.providers.base_provider import BaseProvider


class DeepSeekProvider(BaseProvider):

    def generate(self, prompt: str):

        return {
            "provider": "DeepSeek",
            "prompt": prompt,
            "status": "ready"
        }


deepseek_provider = DeepSeekProvider()

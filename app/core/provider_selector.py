"""
Conclik Pilot AI
Version : 4.3.0
Module : Provider Selector
"""


class ProviderSelector:

    def select(self):

        return {
            "provider": "gemini",
            "model": "default",
        }


provider_selector = ProviderSelector()

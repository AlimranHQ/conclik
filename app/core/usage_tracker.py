"""
Conclik Pilot AI
Version : 4.5.1
Module : Usage Tracker
"""


class UsageTracker:

    def track(self, provider: str, tokens: int):

        return {
            "provider": provider,
            "tokens": tokens,
        }


usage_tracker = UsageTracker()

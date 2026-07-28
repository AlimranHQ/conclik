"""
Conclik Pilot AI
Version : 5.3.0
Module : Rate Limiter
"""


class RateLimiter:

    def allow(
        self,
        identifier: str,
    ) -> bool:

        return True


rate_limiter = RateLimiter()

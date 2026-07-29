"""
Conclik Pilot AI
Provider Score
Version : 1.0.0
"""

from dataclasses import dataclass


@dataclass
class ProviderScore:

    provider: str

    quality: int = 100

    reliability: int = 100

    speed: int = 100

    cost: int = 100

    health: bool = True

    @property
    def total_score(self) -> int:

        return (
            self.quality
            + self.reliability
            + self.speed
            + self.cost
        )


provider_scores = {}


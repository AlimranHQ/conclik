"""
Conclik Pilot AI
Version : 4.5.1
Module : Cost Estimator
"""


class CostEstimator:

    def estimate(self, tokens: int):

        return {
            "tokens": tokens,
            "estimated_cost": 0.0,
        }


cost_estimator = CostEstimator()

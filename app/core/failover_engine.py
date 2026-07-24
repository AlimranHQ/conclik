"""
Conclik Pilot AI
Version : 4.4.0
Module : Failover Engine
"""

from app.core.load_balancer import load_balancer


class FailoverEngine:

    def provider(self):
        return load_balancer.next_provider()


failover_engine = FailoverEngine()

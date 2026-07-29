"""
Conclik Pilot AI
Version : 4.4.0
Module : Load Balancer
"""

from app.core.auto_provider import auto_provider


class LoadBalancer:

    def next_provider(self):
        return auto_provider.select()


load_balancer = LoadBalancer()

"""
Conclik Pilot AI
Version : 4.2.0
Module  : Background Worker
"""

from app.core.workflow_executor import executor


class BackgroundWorker:

    def start(self):
        return executor.execute()


worker = BackgroundWorker()

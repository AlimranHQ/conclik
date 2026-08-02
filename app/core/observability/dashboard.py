"""
Conclik Observability Dashboard
"""

from app.core.collaboration.event_log.event_log import event_log
from app.core.collaboration.trace.event_trace import event_trace


class ObservabilityDashboard:

    async def status(self):

        logs = await event_log.read()
        latest = await event_trace.latest()

        return {
            "status": "dashboard_ready",
            "total_events": len(logs),
            "latest": latest,
            "history": [
                item["type"]
                for item in logs
            ],
        }


dashboard = ObservabilityDashboard()

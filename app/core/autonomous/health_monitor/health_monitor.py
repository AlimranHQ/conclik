"""
Autonomous Health Monitor V1
"""


from datetime import datetime, timezone



class HealthStatus:

    HEALTHY = "healthy"

    DEGRADED = "degraded"

    FAILED = "failed"



class HealthMonitor:


    def __init__(self):

        self.components = {}



    async def register(
        self,
        component
    ):

        self.components[component] = {
            "status": HealthStatus.HEALTHY,
            "failures": 0,
            "heartbeat": datetime.now(timezone.utc),
        }


        return {
            "component": component,
            "status": "registered",
        }



    async def heartbeat(
        self,
        component
    ):

        if component not in self.components:

            return {
                "status": "not_found"
            }


        self.components[component]["heartbeat"] = (
            datetime.now(timezone.utc)
        )


        return {
            "component": component,
            "status": "alive",
        }



    async def report_failure(
        self,
        component
    ):

        if component not in self.components:

            await self.register(component)


        self.components[component]["failures"] += 1


        if self.components[component]["failures"] >= 3:

            self.components[component]["status"] = (
                HealthStatus.FAILED
            )

        else:

            self.components[component]["status"] = (
                HealthStatus.DEGRADED
            )


        return self.components[component]



    async def status(
        self
    ):

        return self.components



    async def system_health(
        self
    ):

        states = [
            item["status"]
            for item in self.components.values()
        ]


        if HealthStatus.FAILED in states:

            return HealthStatus.FAILED


        if HealthStatus.DEGRADED in states:

            return HealthStatus.DEGRADED


        return HealthStatus.HEALTHY



    async def clear(
        self
    ):

        self.components.clear()


        return {
            "status": "cleared"
        }



health_monitor = HealthMonitor()

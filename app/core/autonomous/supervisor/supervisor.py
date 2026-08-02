"""
Autonomous Supervisor V1
"""

from app.core.autonomous.health_monitor.health_monitor import (
    health_monitor,
    HealthStatus,
)

from app.core.autonomous.self_healing.self_healing_engine import (
    self_healing_engine,
)



class Supervisor:


    def __init__(self):

        self.mode = "active"
        self.events = []



    async def register_component(
        self,
        component
    ):

        result = await health_monitor.register(
            component
        )

        self.events.append(
            {
                "action": "register",
                "component": component,
            }
        )

        return result



    async def inspect(
        self
    ):

        health = await health_monitor.system_health()


        return {
            "mode": self.mode,
            "health": health,
        }



    async def supervise_failure(
        self,
        task_id,
        error
    ):

        result = await self_healing_engine.heal(
            task_id,
            error
        )


        self.events.append(
            {
                "action": "healing",
                "task": task_id,
                "status": result["status"],
            }
        )


        return result



    async def decision(
        self
    ):

        health = await health_monitor.system_health()


        if health == HealthStatus.FAILED:

            return {
                "decision": "recovery_required"
            }


        if health == HealthStatus.DEGRADED:

            return {
                "decision": "heal"
            }


        return {
            "decision": "continue"
        }



    async def history(
        self
    ):

        return self.events



    async def clear(
        self
    ):

        self.mode = "active"
        self.events.clear()


        await health_monitor.clear()

        await self_healing_engine.clear()


        return {
            "status": "cleared"
        }



supervisor = Supervisor()

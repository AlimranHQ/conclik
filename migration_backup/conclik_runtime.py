from app.core.runtime_orchestrator.runtime_orchestrator import runtime_orchestrator


class ConclikRuntime:

    async def run(self, goal):

        runtime = await runtime_orchestrator.run(goal)

        return {
            "status": "conclik_ready",
            "runtime": runtime,
        }


conclik_runtime = ConclikRuntime()

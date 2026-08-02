from app.core.runtime_orchestrator.runtime_orchestrator import runtime_orchestrator


class AIRuntime:

    async def run(self, goal):

        runtime = await runtime_orchestrator.run(goal)

        return {
            "status": "runtime_ready",
            "runtime": runtime,
        }


ai_runtime = AIRuntime()

# Backward Compatibility
ConclikRuntime = AIRuntime
conclik_runtime = ai_runtime

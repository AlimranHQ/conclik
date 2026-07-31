from app.core.brain.runtime.brain_runtime import brain_runtime


class RuntimeOrchestrator:

    async def run(self, goal):

        brain = await brain_runtime.run(goal)

        return {
            "status": "runtime_completed",
            "goal": goal,
            "brain": brain,
        }


runtime_orchestrator = RuntimeOrchestrator()

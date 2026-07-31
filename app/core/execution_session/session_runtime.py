from app.core.context_bus.context_runtime import context_runtime


class SessionRuntime:

    async def create(self, goal):

        await context_runtime.set(
            "goal",
            goal,
        )

        return {
            "session_id": "SESSION-001",
            "status": "running",
            "goal": goal,
        }


session_runtime = SessionRuntime()

from app.core.persistent_memory.memory_runtime import memory_runtime as persistent_memory_runtime


class MemoryRuntime:

    async def remember(self, key, value):

        try:
            await persistent_memory_runtime.remember(
                key,
                value
            )
            return True

        except Exception:
            return False


    async def recall(self, goal: str):

        try:
            memory = await persistent_memory_runtime.recall(
                goal
            )

        except Exception:
            memory = {}

        return {
            "status": "memory_ready",
            "memory": memory or {},
            "goal": goal,
        }


memory_runtime = MemoryRuntime()

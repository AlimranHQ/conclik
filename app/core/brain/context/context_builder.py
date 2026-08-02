from app.core.brain.memory.memory_runtime import memory_runtime
from app.core.brain.conversation.memory.conversation_memory import conversation_memory


class ContextBuilder:

    async def build(self, goal):

        long_memory = await memory_runtime.search(goal)

        conversation = await conversation_memory.recall()

        return {
            "status": "context_ready",
            "goal": goal,
            "conversation": conversation["history"],
            "memory": long_memory["results"],
            "conversation_count": len(conversation["history"]),
            "memory_count": long_memory["count"],
        }


context_builder = ContextBuilder()

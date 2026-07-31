from app.core.kernel.base_engine import BaseEngine

from app.core.brain.personality.personality_runtime import personality_runtime
from app.core.brain.memory.memory_runtime import memory_runtime
from app.core.reflection_engine.reflection_runtime import reflection_runtime


class ConversationEngine(BaseEngine):

    async def respond(self, goal: str):

        personality = await personality_runtime.run(goal)

        memory = await memory_runtime.recall(goal)

        reflection = await reflection_runtime.run(True)

        return {
            "status": "response_ready",
            "identity": personality["personality"]["identity"],
            "emotion": personality["emotion"],
            "memory": memory,
            "reflection": reflection,
            "response":
                f"[{personality['emotion']}] "
                f"I am {personality['personality']['name']}.\n"
                f"I remember previous context.\n"
                f"Reflection: {reflection['reflection']}\n"
                f"Ready to execute: {goal}",
        }

    async def run(self, goal: str):
        return await self.respond(goal)


conversation_engine = ConversationEngine()

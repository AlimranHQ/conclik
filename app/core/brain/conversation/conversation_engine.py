from app.core.brain.context.context_builder import context_builder
from app.core.brain.conversation.memory.conversation_memory import (
    conversation_memory,
)


class ConversationEngine:

    async def run(self, goal):

        context = await context_builder.build(goal)

        response = {
            "status": "response_ready",
            "goal": goal,
            "context": context,
            "response": (
                f"Ready to execute: {goal}\n"
                f"Conversation Memory: {context['conversation_count']}\n"
                f"Long Memory: {context['memory_count']}"
            ),
        }

        await conversation_memory.remember(
            "user",
            goal,
        )

        await conversation_memory.remember(
            "assistant",
            response["response"],
        )

        return response


conversation_engine = ConversationEngine()

class ConversationMemory:

    def __init__(self):
        self.history = []

    async def remember(self, role, message):

        self.history.append({
            "role": role,
            "message": message,
        })

        return {
            "status": "conversation_saved",
        }

    async def recall(self, limit=10):

        return {
            "status": "conversation_ready",
            "history": self.history[-limit:],
        }


conversation_memory = ConversationMemory()

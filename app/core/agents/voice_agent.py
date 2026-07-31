class VoiceAgent:
    async def run(self, goal):
        return {
            "status": "completed",
            "agent": "voice_agent",
            "goal": goal,
            "result": f"Voice completed for: {goal}",
        }

voice_agent = VoiceAgent()

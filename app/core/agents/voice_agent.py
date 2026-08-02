from app.core.agents.base_agent import BaseAgent


class VoiceAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "voice_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"Voice completed for: {goal}",
        }


voice_agent = VoiceAgent()

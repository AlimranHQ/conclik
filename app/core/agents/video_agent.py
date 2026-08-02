from app.core.agents.base_agent import BaseAgent


class VideoAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "video_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"Video completed for: {goal}",
        }


video_agent = VideoAgent()

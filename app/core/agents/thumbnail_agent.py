from app.core.agents.base_agent import BaseAgent


class ThumbnailAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "thumbnail_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"Thumbnail completed for: {goal}",
        }


thumbnail_agent = ThumbnailAgent()

from app.core.agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "research_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"Research completed for: {goal}",
        }


research_agent = ResearchAgent()

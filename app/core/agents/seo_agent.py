from app.core.agents.base_agent import BaseAgent


class SEOAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "seo_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"SEO completed for: {goal}",
        }


seo_agent = SEOAgent()

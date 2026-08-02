from app.core.agents.base_agent import BaseAgent
from app.core.collaboration.event_bus.publisher import publisher


class ResearchAgent(BaseAgent):

    @property
    def name(self):
        return "research_agent"

    async def run(self, goal):

        result = {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"Research completed for: {goal}",
        }

        await publisher.publish(
            "research_completed",
            self.name,
            result,
        )

        return result


research_agent = ResearchAgent()

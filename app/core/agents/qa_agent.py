from app.core.agents.base_agent import BaseAgent


class QAAgent(BaseAgent):

    @property
    def name(self) -> str:
        return "qa_agent"

    async def run(self, goal: str):

        return {
            "status": "completed",
            "agent": self.name,
            "goal": goal,
            "result": f"QA completed for: {goal}",
        }


qa_agent = QAAgent()

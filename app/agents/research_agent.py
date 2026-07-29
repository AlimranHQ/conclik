"""
Conclik Pilot AI
Research Agent
Version : 6.0.0
Architecture : Base Agent
"""

from app.core.agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    def __init__(self):
        super().__init__(provider="gemini")

    async def analyze(
        self,
        topic: str,
    ) -> str:

        prompt = f"""
You are an expert Content Research Agent.

Topic:
{topic}

Please provide:

1. Key insights
2. Important trends
3. Audience interests
4. Reliable talking points

Keep the response professional.
"""

        try:
            return await self.ask_ai(
                prompt=prompt,
                category="research",
            )

        except Exception as e:
            raise Exception(
                f"Research Agent Error: {e}"
            )

    async def run(
        self,
        topic: str,
    ):
        return await self.analyze(topic)


research_agent = ResearchAgent()


"""
Conclik Pilot AI - Research Agent
Version: 6.0.0
"""

from app.core.agents.base_agent import BaseAgent
from app.core.providers.provider_manager import provider_manager


class ResearchAgent(BaseAgent):

    @property
    def name(self):
        return "research"

    async def analyze(self, topic: str):

        prompt = f"""
You are an expert Content Research Agent.

Topic:
{topic}

Provide:

1. Key insights
2. Trends
3. Audience interests
4. Talking points
"""

        return await provider_manager.generate(
            provider_name="gemini",
            prompt=prompt,
        )

    async def run(self, topic: str):
        return await self.analyze(topic)


research_agent = ResearchAgent()

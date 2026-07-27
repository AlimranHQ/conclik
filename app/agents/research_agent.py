"""
Conclik Pilot AI - Research Agent
Version: 5.0.0
"""

from app.providers.gemini_client import gemini_client

class ResearchAgent:
    async def analyze(self, topic: str) -> str:
        prompt = f"""
        You are an expert Content Research Agent. Your task is to research the given topic thoroughly.
        Topic: {topic}

        Please provide:
        1. Key insights and core concepts.
        2. Important sub-topics or trends.
        3. Target audience interest points.
        4. Reliable talking points for content creation.

        Keep the response well-structured, clear, and professional.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"Research Agent Error: {str(e)}")

research_agent = ResearchAgent()

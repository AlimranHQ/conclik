import logging
from typing import Dict, Any, List
from app.providers.gemini_client import GeminiClient  # আপনার বর্তমান জেমিনি ক্লায়েন্ট ব্যবহার করা হচ্ছে

logger = logging.getLogger(__name__)

class ResearchAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = (
            "You are an expert Research Agent in the Conclik AI multi-agent system. "
            "Your job is to analyze the given topic, gather deep insights, find key talking points, "
            "identify target audience interests, and provide structured research data."
        )

    async def execute_research(self, topic: str, target_audience: str = "General") -> Dict[str, Any]:
        """
        Executes deep research on a given topic using the latest AI models.
        """
        try:
            prompt = (
                f"Topic: {topic}\n"
                f"Target Audience: {target_audience}\n\n"
                "Please provide a comprehensive research report including:\n"
                "1. Executive Summary\n"
                "2. Key Talking Points & Subtopics\n"
                "3. Trending Angles / Insights\n"
                "4. Suggested Keywords / Tags for SEO"
            )

            # জেমিনি ক্লায়েন্ট বা এআই গেটওয়ে ব্যবহার করে রিকোয়েস্ট পাঠানো
            response = await self.client.generate_content(
                prompt=prompt,
                system_instruction=self.system_prompt
            )

            return {
                "status": "success",
                "topic": topic,
                "research_data": response
            }
        except Exception as e:
            logger.error(f"Error in ResearchAgent: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }

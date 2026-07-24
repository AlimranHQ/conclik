import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class QAAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = "You are an expert Quality Assurance (QA) Agent. You review multi-agent outputs for factual accuracy, quality, and coherence."

    async def review_content(self, content_package: str) -> Dict[str, Any]:
        try:
            prompt = f"Content Package to Review:\n{content_package}\n\nPerform a thorough quality check, verify coherence, fix any weak hooks or formatting flaws, and provide a final approval score."
            response = await self.client.generate_content(prompt, system_instruction=self.system_prompt)
            return {"status": "success", "qa_report": response}
        except Exception as e:
            logger.error(f"Error in QAAgent: {str(e)}")
            return {"status": "error", "message": str(e)}

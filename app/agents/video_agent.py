import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class VideoAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = "You are an expert Video Production Agent. You create scene-by-scene storyboard layouts and visual cue directions."

    async def generate_storyboard(self, script: str) -> Dict[str, Any]:
        try:
            prompt = f"Script:\n{script}\n\nCreate a scene-by-scene storyboard breakdown including visual descriptions, B-roll suggestions, and transitions."
            response = await self.client.generate_content(prompt, system_instruction=self.system_prompt)
            return {"status": "success", "storyboard": response}
        except Exception as e:
            logger.error(f"Error in VideoAgent: {str(e)}")
            return {"status": "error", "message": str(e)}

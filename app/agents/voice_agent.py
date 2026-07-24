import logging
from typing import Dict, Any
from app.providers.gemini_client import GeminiClient

logger = logging.getLogger(__name__)

class VoiceAgent:
    def __init__(self):
        self.client = GeminiClient()
        self.system_prompt = "You are an expert Voice & Audio Agent. You optimize text-to-speech pacing, emotional tone markers, and voice direction."

    async def optimize_for_voice(self, script: str) -> Dict[str, Any]:
        try:
            prompt = f"Script:\n{script}\n\nOptimize this script for Text-to-Speech (TTS) by adding audio pauses [pause], emotional cues, and voice modulation markers."
            response = await self.client.generate_content(prompt, system_instruction=self.system_prompt)
            return {"status": "success", "voice_script": response}
        except Exception as e:
            logger.error(f"Error in VoiceAgent: {str(e)}")
            return {"status": "error", "message": str(e)}

"""
Conclik Pilot AI - Script Agent
Version: 5.0.0
"""

import google.generativeai as genai
from app.providers.gemini_client import gemini_client

class ScriptAgent:
    async def generate_script(self, topic: str, research_data: str) -> str:
        prompt = f"""
        You are an expert Video Script Writer. Your task is to write an engaging, high-retention script based on the provided research.
        Topic: {topic}
        
        Research Insights:
        {research_data}

        Please structure the script with:
        1. Hook (0-5 seconds): Catchy opening to grab attention.
        2. Introduction: Briefly introduce what will be covered.
        3. Body Content: Main talking points broken down smoothly.
        4. Call to Action (CTA) & Outro: Engaging closing.

        Keep the tone natural, professional, and conversational.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"Script Agent Error: {str(e)}")

script_agent = ScriptAgent()

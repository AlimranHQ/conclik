"""
Conclik Pilot AI - SEO Agent
Version: 5.0.0
Description: Generates optimized SEO titles, descriptions, tags, and hashtags.
"""

import google.generativeai as genai
from app.providers.gemini_client import gemini_client

class SEOAgent:
    async def optimize(self, topic: str, research_data: str, script_data: str) -> str:
        prompt = f"""
        You are an expert YouTube and Content SEO Specialist. Your task is to generate high-performing SEO metadata based on the provided topic, research, and script.
        
        Topic: {topic}
        
        Research Summary:
        {research_data}

        Script Content:
        {script_data}

        Please provide:
        1. Catchy & High-CTR Video Titles (Provide 3 options).
        2. SEO-Optimized Video Description (With timestamps placeholder and keywords).
        3. Relevant Tags (Comma-separated for search ranking).
        4. Trending Hashtags (Top 5-10 hashtags).

        Keep the output structured, clean, and ready to use.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"SEO Agent Error: {str(e)}")

seo_agent = SEOAgent()

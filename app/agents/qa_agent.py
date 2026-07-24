"""
Conclik Pilot AI - QA (Quality Assurance) Agent
Version: 5.0.0
Description: Reviews all generated content across agents, checks for quality, consistency, and provides final polish.
"""

import google.generativeai as genai
from app.providers.gemini_client import gemini_client

class QAAgent:
    async def review_quality(self, topic: str, all_outputs: dict) -> str:
        prompt = f"""
        You are an expert Content Quality Assurance (QA) Director and Senior Editor. Your task is to review the complete multi-agent pipeline output for the given topic and ensure everything is cohesive, professional, and high-quality.
        
        Topic: {topic}

        Pipeline Outputs to Review:
        - Research: {all_outputs.get('research', {}).get('output', 'N/A')}
        - Script: {all_outputs.get('script', {}).get('output', 'N/A')}
        - SEO: {all_outputs.get('seo', {}).get('output', 'N/A')}
        - Thumbnail: {all_outputs.get('thumbnail', {}).get('output', 'N/A')}
        - Voice: {all_outputs.get('voice', {}).get('output', 'N/A')}
        - Video: {all_outputs.get('video', {}).get('output', 'N/A')}

        Please provide:
        1. Overall Quality Score (Out of 10) and Summary.
        2. Consistency Check (Do the script, SEO, and visual elements align well with the research?).
        3. Constructive Feedback or Areas of Improvement for each section.
        4. Final Approval Status (Ready for production or needs minor tweaks).

        Keep the tone professional, objective, and expert-level.
        """
        
        try:
            response = await gemini_client.generate_content(prompt)
            return response
        except Exception as e:
            raise Exception(f"QA Agent Error: {str(e)}")

qa_agent = QAAgent()

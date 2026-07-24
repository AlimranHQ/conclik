import logging
from typing import Dict, Any
from app.agents.research_agent import ResearchAgent
from app.agents.script_agent import ScriptAgent
from app.agents.seo_agent import SEOAgent
from app.agents.thumbnail_agent import ThumbnailAgent
from app.agents.voice_agent import VoiceAgent
from app.agents.video_agent import VideoAgent
from app.agents.qa_agent import QAAgent

logger = logging.getLogger(__name__)

class MultiAgentOrchestrator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.script_agent = ScriptAgent()
        self.seo_agent = SEOAgent()
        self.thumbnail_agent = ThumbnailAgent()
        self.voice_agent = VoiceAgent()
        self.video_agent = VideoAgent()
        self.qa_agent = QAAgent()

    async def run_pipeline(self, topic: str, tone: str = "Engaging") -> Dict[str, Any]:
        """
        Runs the complete v5.0 Multi-Agent Pipeline from Research to QA.
        """
        try:
            logger.info(f"Starting Multi-Agent Pipeline for topic: {topic}")

            # Step 1: Research (Fixed method call)
            research_res = await self.research_agent.execute_research(topic=topic)
            research_text = research_res.get("research_data", "") if isinstance(research_res, dict) else str(research_res)

            # Step 2: Script Generation
            script_res = await self.script_agent.generate_script(topic=topic, research_data=research_text, tone=tone)
            script_text = script_res.get("script", "")

            # Step 3: SEO Optimization
            seo_res = await self.seo_agent.optimize_content(title=topic, content=script_text)

            # Step 4: Thumbnail Ideas
            thumbnail_res = await self.thumbnail_agent.generate_thumbnail_ideas(title=topic, script_summary=script_text[:500])

            # Step 5: Voice Optimization
            voice_res = await self.voice_agent.optimize_for_voice(script=script_text)

            # Step 6: Video Storyboard
            video_res = await self.video_agent.generate_storyboard(script=script_text)

            # Step 7: Final QA Review
            combined_package = f"Script:\n{script_text}\n\nSEO Data:\n{seo_res}\n\nThumbnail:\n{thumbnail_res}"
            qa_res = await self.qa_agent.review_content(content_package=combined_package)

            return {
                "status": "success",
                "topic": topic,
                "research": research_res,
                "script": script_res,
                "seo": seo_res,
                "thumbnail": thumbnail_res,
                "voice": voice_res,
                "video": video_res,
                "qa": qa_res
            }

        except Exception as e:
            logger.error(f"Error in MultiAgentOrchestrator: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }

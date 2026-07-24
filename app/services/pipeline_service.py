"""
Conclik Pilot AI
Version : 5.0.0
Module : Complete Multi-Agent Pipeline Service (Research to QA)
"""

import asyncio
from app.agents.research_agent import research_agent
from app.agents.script_agent import script_agent
from app.agents.seo_agent import seo_agent
from app.agents.thumbnail_agent import thumbnail_agent
from app.agents.voice_agent import voice_agent
from app.agents.video_agent import video_agent
from app.agents.qa_agent import qa_agent

class PipelineService:
    async def run_pipeline(self, topic: str):
        results = {"status": "success", "topic": topic}
        
        try:
            # Step 1: Research Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            research_output = await research_agent.analyze(topic)
            results["research"] = {
                "status": "success",
                "output": research_output
            }
            
            # Step 2: Script Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            script_output = await script_agent.generate_script(topic, research_output)
            results["script"] = {
                "status": "success",
                "output": script_output
            }

            # Step 3: SEO Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            seo_output = await seo_agent.optimize(topic, research_output, script_output)
            results["seo"] = {
                "status": "success",
                "output": seo_output
            }

            # Step 4: Thumbnail Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            thumbnail_output = await thumbnail_agent.design_concept(topic, research_output, script_output)
            results["thumbnail"] = {
                "status": "success",
                "output": thumbnail_output
            }

            # Step 5: Voice Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            voice_output = await voice_agent.create_voice_guideline(topic, script_output)
            results["voice"] = {
                "status": "success",
                "output": voice_output
            }

            # Step 6: Video Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            video_output = await video_agent.create_storyboard(topic, script_output, voice_output)
            results["video"] = {
                "status": "success",
                "output": video_output
            }

            # Step 7: QA Agent
            await asyncio.sleep(4)  # Free tier rate-limit handler
            qa_output = await qa_agent.review_quality(topic, results)
            results["qa"] = {
                "status": "success",
                "output": qa_output
            }
            
        except Exception as e:
            # Determining which step failed for better debugging
            failed_step = "unknown"
            if "research" not in results or results["research"]["status"] == "error":
                failed_step = "research"
            elif "script" not in results or results["script"]["status"] == "error":
                failed_step = "script"
            elif "seo" not in results or results["seo"]["status"] == "error":
                failed_step = "seo"
            elif "thumbnail" not in results or results["thumbnail"]["status"] == "error":
                failed_step = "thumbnail"
            elif "voice" not in results or results["voice"]["status"] == "error":
                failed_step = "voice"
            elif "video" not in results or results["video"]["status"] == "error":
                failed_step = "video"
            else:
                failed_step = "qa"
                
            results[failed_step] = {
                "status": "error",
                "message": str(e)
            }
            
        return results

pipeline_service = PipelineService()

from app.analyzers.video_analyzer import video_analyzer
from app.analyzers.transcript_analyzer import transcript_analyzer
from app.analyzers.viral_score import viral_score
from app.analyzers.scene_engine import scene_engine
from app.analyzers.thumbnail_prompt_engine import thumbnail_prompt_engine


class AnalysisService:

    def analyze(
        self,
        topic: str,
        duration: int = 10,
    ):

        video = video_analyzer.analyze(
            topic=topic,
            duration=duration,
        )

        transcript = transcript_analyzer.analyze(
            audio_source="future_audio_file"
        )

        score = viral_score.analyze(
            title=topic,
            description=f"Complete guide and tutorial about {topic}. Learn everything you need to know step by step.",
            hashtags=["#ai", "#tutorial", "#viral"],
        )

        # Generate scenes using the Scene Engine
        scenes_data = scene_engine.generate_scenes(
            topic=topic,
            duration=duration,
        )

        # Generate thumbnail & image prompts using the new Thumbnail Prompt Engine
        thumbnail_prompts = thumbnail_prompt_engine.generate_prompts(
            topic=topic,
            scene_details=f"Core concept and highlight scenes for {topic}"
        )

        return {
            "success": True,

            "topic": topic,

            "video_analysis": video,

            "transcript_analysis": transcript,

            "viral_analysis": score,

            "scene_analysis": scenes_data,

            "thumbnail_analysis": thumbnail_prompts,

            "status": "Master Analysis Completed with Thumbnail Prompt Engine"
        }


analysis_service = AnalysisService()

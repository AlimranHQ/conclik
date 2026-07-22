from app.analyzers.video_analyzer import video_analyzer
from app.analyzers.transcript_analyzer import transcript_analyzer
from app.analyzers.viral_score import viral_score


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
            description="Future Generated Description",
            hashtags=[],
        )

        return {
            "success": True,

            "topic": topic,

            "video_analysis": video,

            "transcript_analysis": transcript,

            "viral_analysis": score,

            "status": "Master Analysis Completed"
        }


analysis_service = AnalysisService()

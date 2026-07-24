"""
Conclik v5.1
AI Director
"""

from app.pipeline.pipeline_manager import pipeline_manager


class Director:

    def execute(self, prompt: str):

        workflow = [
            "research",
            "script",
            "seo",
            "thumbnail",
            "qa",
        ]

        results = {}

        for agent in workflow:
            results[agent] = pipeline_manager.run(
                {
                    "agent": agent,
                    "prompt": prompt,
                }
            )

        return results


director = Director()

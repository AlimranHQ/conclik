"""
Conclik Pilot AI
Version : 4.3.0
Module  : Prompt Optimizer
"""

from app.core.context_engine import context_engine


class PromptOptimizer:

    def optimize(
        self,
        prompt: str,
        project: str = "default",
    ):

        context = context_engine.build_context(
            prompt,
            project,
        )

        return {
            "prompt": prompt,
            "context": context,
            "optimized_prompt": context,
        }


prompt_optimizer = PromptOptimizer()

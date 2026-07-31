class ReflectionAnalyzer:

    async def analyze(self, result):

        score = 100 if result else 0

        return {
            "score": score,
            "reflection": (
                "Execution successful."
                if score == 100
                else "Execution failed."
            ),
        }


reflection_analyzer = ReflectionAnalyzer()

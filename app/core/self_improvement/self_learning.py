class SelfLearning:

    async def improve(self, reflection):

        if reflection.get("score", 0) >= 90:
            action = "Keep current strategy"
        else:
            action = "Adjust execution strategy"

        return {
            "previous_score": reflection.get("score", 0),
            "action": action,
            "improved": True,
        }


self_learning = SelfLearning()

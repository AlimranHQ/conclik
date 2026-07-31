class GoalClassifier:

    async def classify(self, goal: str):

        text = goal.lower()

        if "youtube" in text:
            return "content"

        if "ai" in text:
            return "artificial_intelligence"

        if "website" in text:
            return "software"

        return "general"


goal_classifier = GoalClassifier()

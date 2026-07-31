class EmotionProfile:

    def detect(self, goal: str):

        text = goal.lower()

        if "urgent" in text:
            return "URGENT"

        if "optimize" in text:
            return "OPTIMIZATION"

        if "learn" in text:
            return "LEARNING"

        if "creative" in text:
            return "CREATIVE"

        return "ANALYTICAL"


emotion_profile = EmotionProfile()

class GoalDecomposer:

    async def decompose(self, goal: str):

        goal_lower = goal.lower()

        if "youtube" in goal_lower:
            return [
                "Research",
                "Planning",
                "Script",
                "SEO",
                "Thumbnail",
                "Voice",
                "Video",
                "QA",
                "Publish",
            ]

        if "website" in goal_lower:
            return [
                "Requirement Analysis",
                "Architecture",
                "Backend",
                "Frontend",
                "Database",
                "Testing",
                "Deployment",
            ]

        return [
            "Research",
            "Planning",
            "Execution",
        ]


goal_decomposer = GoalDecomposer()

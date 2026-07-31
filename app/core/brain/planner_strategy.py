class PlannerStrategy:

    async def build(self, goal: str):

        return {
            "mission": goal,
            "strategy": [
                "Research",
                "Planning",
                "Production",
                "Quality Assurance",
                "Publishing",
                "Optimization",
            ],
        }


planner_strategy = PlannerStrategy()

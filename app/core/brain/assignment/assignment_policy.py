class AssignmentPolicy:

    async def build(self, plan):

        mapping = {
            "Research": "research_agent",
            "Planning": "research_agent",
            "Production": "video_agent",
            "Quality Assurance": "qa_agent",
            "Publishing": "qa_agent",
            "Optimization": "seo_agent",
        }

        assignments = []

        for node in plan["graph"]:

            assignments.append(
                {
                    "task": node["task"],
                    "agent": mapping.get(
                        node["task"],
                        "research_agent",
                    ),
                    "depends_on": node["depends_on"],
                }
            )

        return assignments


assignment_policy = AssignmentPolicy()

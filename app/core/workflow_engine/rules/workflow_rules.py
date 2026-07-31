class WorkflowRules:

    def apply(self, assignments):

        sequential = []
        parallel = []

        for item in assignments:

            if item["depends_on"]:
                sequential.append(item)

            else:
                parallel.append(item)

        return {
            "parallel": parallel,
            "sequential": sequential,
        }


workflow_rules = WorkflowRules()

class GoalCompletionChecker:

    def check(self, brain_result):

        reflection = brain_result["reflection"]["reflection"]
        workflow = brain_result["workflow"]["execution"]

        score = reflection.get("score", 0)

        failed = workflow.get("failed", [])

        completed = workflow.get("completed", [])

        completed_count = len(completed)

        if failed:
            return {
                "status": "replan",
                "reason": "workflow_failed",
            }

        if score >= 90 and completed_count > 0:
            return {
                "status": "goal_completed",
                "reason": "all_checks_passed",
            }

        return {
            "status": "continue",
            "reason": "needs_more_work",
        }


goal_completion_checker = GoalCompletionChecker()

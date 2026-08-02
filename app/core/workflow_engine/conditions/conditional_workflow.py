from app.core.workflow_engine.conditions.condition_engine import condition_engine


class ConditionalWorkflow:

    def resolve(self, node, context):

        if "condition" not in node:
            return node["next"]

        ok = condition_engine.evaluate(
            node["condition"],
            context
        )

        if ok:
            return node["true"]

        return node["false"]


conditional_workflow = ConditionalWorkflow()

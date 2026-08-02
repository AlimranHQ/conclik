class ConditionEngine:

    def evaluate(self, condition, context):

        value = context.get(condition["field"])

        operator = condition["operator"]

        target = condition["value"]

        if operator == "==":
            return value == target

        if operator == "!=":
            return value != target

        if operator == ">":
            return value > target

        if operator == "<":
            return value < target

        if operator == ">=":
            return value >= target

        if operator == "<=":
            return value <= target

        return False


condition_engine = ConditionEngine()

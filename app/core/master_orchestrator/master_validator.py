"""
Master Validator V1
"""


class MasterValidator:

    def validate(self, goal):

        if goal is None:
            return False

        if not isinstance(goal, str):
            return False

        if not goal.strip():
            return False

        return True


master_validator = MasterValidator()

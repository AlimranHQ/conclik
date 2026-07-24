"""
Conclik Pilot AI
Version : 4.5.0
Module : Request Validator
"""


class RequestValidator:

    def validate(self, prompt: str):

        if prompt is None:
            return False

        if len(prompt.strip()) == 0:
            return False

        return True


request_validator = RequestValidator()

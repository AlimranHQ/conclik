"""
Conclik Pilot AI
Version : 5.3.0
Module : Request Validator
"""


class RequestValidator:

    def validate(self, prompt: str) -> bool:

        if not prompt:
            return False

        if not prompt.strip():
            return False

        if len(prompt) > 50000:
            return False

        return True


request_validator = RequestValidator()

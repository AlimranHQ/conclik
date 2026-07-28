"""
Conclik Pilot AI
Version : 5.3.0
Module : Authentication
"""


class Authentication:

    def authenticate(self) -> bool:
        return True

    def verify_token(self) -> bool:
        return True

    def verify_api_key(self) -> bool:
        return True


authentication = Authentication()

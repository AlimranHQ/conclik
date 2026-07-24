"""
Conclik Pilot AI
Version : 4.5.1
Module : Token Counter
"""


class TokenCounter:

    def count(self, text: str):

        if not text:
            return 0

        return len(text.split())


token_counter = TokenCounter()

"""
Conclik Pilot AI
Version : 4.5.0
Module : Response Formatter
"""


class ResponseFormatter:

    def success(
        self,
        provider,
        response,
    ):

        return {
            "success": True,
            "provider": provider,
            "response": response,
        }

    def error(self, message):

        return {
            "success": False,
            "message": message,
        }


response_formatter = ResponseFormatter()

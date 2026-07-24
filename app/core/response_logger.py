"""
Conclik Pilot AI
Version : 4.5.1
Module : Response Logger
"""

import datetime


class ResponseLogger:

    def log(self, response):

        return {
            "time": datetime.datetime.utcnow().isoformat(),
            "response": response,
        }


response_logger = ResponseLogger()

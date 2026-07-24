"""
Conclik Pilot AI
Version : 4.5.1
Module : Request Logger
"""

import datetime


class RequestLogger:

    def log(self, prompt: str):

        return {
            "time": datetime.datetime.utcnow().isoformat(),
            "prompt": prompt,
        }


request_logger = RequestLogger()

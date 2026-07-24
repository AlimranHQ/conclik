"""
Conclik Pilot AI
Version : 4.2.0
Module  : Retry Engine
"""


class RetryEngine:

    def retry(self, job):

        return {
            "success": True,
            "job": job,
            "retry": True
        }


retry_engine = RetryEngine()

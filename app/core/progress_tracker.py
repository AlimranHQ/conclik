"""
Conclik Pilot AI
Version : 4.2.0
Module  : Progress Tracker
"""


class ProgressTracker:

    def progress(self, project_id: int):

        return {
            "project_id": project_id,
            "progress": 100,
            "status": "Completed"
        }


tracker = ProgressTracker()

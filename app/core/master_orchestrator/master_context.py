"""
Master Context V1
"""


class MasterContext:

    def __init__(self):

        self.goal = None
        self.session = None
        self.data = {}


    def set_goal(self, goal):

        self.goal = goal


    def set_session(self, session):

        self.session = session


    def update(self, key, value):

        self.data[key] = value


    def get(self, key):

        return self.data.get(key)


    def snapshot(self):

        return {
            "goal": self.goal,
            "session": self.session,
            "data": self.data,
        }


master_context = MasterContext()

"""
Master History V1
"""


class MasterHistory:

    def __init__(self):

        self.records = []


    def add(self, entry):

        self.records.append(entry)


    def all(self):

        return self.records


    def clear(self):

        self.records.clear()


master_history = MasterHistory()

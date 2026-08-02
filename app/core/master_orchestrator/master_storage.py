"""
Master Storage V1
"""


class MasterStorage:

    def __init__(self):

        self.storage = {}


    def save(self, key, value):

        self.storage[key] = value


    def load(self, key):

        return self.storage.get(key)


    def all(self):

        return self.storage


master_storage = MasterStorage()

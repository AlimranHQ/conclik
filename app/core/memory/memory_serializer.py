"""
Memory Serializer
"""

import json


class MemorySerializer:

    def serialize(self, data):

        return json.dumps(data)

    def deserialize(self, data):

        return json.loads(data)


memory_serializer = MemorySerializer()


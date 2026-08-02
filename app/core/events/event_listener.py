"""
Conclik Event Listener V2
"""


class EventListener:


    def __init__(self):

        self.events = []


    def listen(self, event):

        self.events.append(event)


    def all(self):

        return self.events



event_listener = EventListener()

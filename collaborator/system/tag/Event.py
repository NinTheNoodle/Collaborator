from .ref import system


class Event(system.base.Tag):
    def create(self, event):
        return event

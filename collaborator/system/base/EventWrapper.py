from functools import partial
from collaborator import Reference
from .ref import system


class EventWrapper(object):
    def __init__(self, package):
        self.package = package

    def __call__(self, func):
        event_class = getattr(self, func.__name__)
        event = event_class()

        def auto_call(owner, name):
            owner.add_tag(system.tag.Event(event))
            if hasattr(event, "owner_create"):
                event.owner_create(owner, name)

        # Automatically called when the event's owner is created
        system.base.GameObject._c_auto_call[func] = auto_call

        if hasattr(event, "wrap"):
            return event.wrap(func)

        return func

    def __getattr__(self, item):
        return Reference(self.package, item)

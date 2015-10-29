from .ref import system


class Enabled(system.base.Tag):
    remove = [system.tag.Disabled]

from .ref import system


class Disabled(system.base.Tag):
    remove = [system.tag.Enabled]

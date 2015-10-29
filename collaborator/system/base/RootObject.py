from collaborator.system.ref import system


class RootObject(system.base.GameObject):
    def __init__(self):
        self.parent = None
        self.parents = {}
        self._c_children = {}
        self._c_tags = {}
        self.create()

    def create(self):
        self.add_tag(system.tag.name.Root())

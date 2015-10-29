from .ref import system
name = system.tag.name


class Game(system.base.GameObject):
    @system.event
    def create(self):
        print(self.parents[name.Root()])
        self.add_tag(system.tag.Enabled())
        print(self.get_tags())
        system.collision.Rectangle(self)

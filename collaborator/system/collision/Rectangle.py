from .ref import system


class Rectangle(system.base.GameObject):
    name = "collidable"

    @system.event
    def create(self):
        print(self)

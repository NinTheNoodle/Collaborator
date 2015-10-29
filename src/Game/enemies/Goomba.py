from . import GameObject


class Goomba(GameObject):
    def on_create(self):
        print self.__module__, __name__, Goomba

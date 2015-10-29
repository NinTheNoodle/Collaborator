class Tag(object):
    remove = []
    conflicts = []
    data = None
    cached = False

    def __init__(self, *args, **kwargs):
        self.data = self.create(*args, **kwargs)

    def __repr__(self):
        if isinstance(self.data, tuple):
            data = ", ".join(repr(x) for x in self.data)
        elif self.data is None:
            data = ""
        else:
            data = repr(self.data)

        return "{}({})".format(self.__class__.__name__, data)

    def create(self):
        return None

    def attach(self, owner):
        pass

    def detach(self, owner):
        pass

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.data == other.data

    def __hash__(self):
        return hash((self.__class__, self.data))

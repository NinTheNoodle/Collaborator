from importlib import import_module


def camel_case(name):
    rtn = []
    word_start = True
    for char in name:
        if not word_start and char == "_":
            word_start = True
        elif word_start:
            rtn.append(char.upper())
            word_start = False
        else:
            rtn.append(char)
    return "".join(rtn)


class Reference(object):
    def __new__(cls, *path_parts):
        path = ".".join(path_parts)
        name = path.rsplit(".", 1)[-1]
        module = import_module(path)
        try:
            return getattr(module, name)
        except AttributeError:
            class_name = camel_case(name)
            try:
                return getattr(module, class_name)
            except AttributeError:
                return super(Reference, cls).__new__(cls)

    def __init__(self, *path_parts):
        self._c_path = ".".join(path_parts)

    def __getattr__(self, item):
        return Reference("{}.{}".format(self._c_path, item))

    def __repr__(self):
        return "<reference '{}'>".format(self._c_path)

    def __call__(self, parent, *args, **kwargs):
        raise TypeError("{} does not contain a class".format(self))

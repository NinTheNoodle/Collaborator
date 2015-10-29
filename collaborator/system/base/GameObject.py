from .ref import system


class GameObject(object):
    _c_auto_call = {}

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.parents = parent.parents.copy()

        for tag in parent.get_tags():
            if tag.cached:
                self.parents[tag] = parent

        self._c_tags = {}

        for name, item in self.__class__.__dict__.items():
            try:
                func = self._c_auto_call[item]
            except (KeyError, TypeError):
                pass
            else:
                func(self, name)

        for cls in self.__class__.mro():
            self.add_tag(system.tag.Class(cls))

        self.create(*args, **kwargs)

    def add_tag(self, tag):
        try:
            self._c_tags[tag.__class__].add(tag)
        except KeyError:
            self._c_tags[tag.__class__] = {tag}

        for conflict in tag.conflicts:
            if self.has_tag(conflict):
                raise TypeError("tag '{}' conflicts with existing tag "
                                "'{}'".format(tag, conflict))

        for removal in tag.remove:
            try:
                self.remove_tag(removal)
            except KeyError:
                pass

        tag.attach(self)

    def has_tag(self, tag):
        if isinstance(tag, system.base.Tag):
            try:
                if tag in self._c_tags[tag.__class__]:
                    return False
            except KeyError:
                pass
        else:
            if tag in self._c_tags:
                return False
        return True

    def get_tag_types(self):
        return self._c_tags.keys()

    def get_tags(self, tag_type=None):
        if tag_type is None:
            return set().union(*self._c_tags.values())
        else:
            return self._c_tags.get(tag_type, set()).copy()

    def remove_tag(self, tag):
        if isinstance(tag, system.base.Tag):
            tag_type = tag.__class__
            tag_instances = {tag}
        else:
            tag_type = tag
            tag_instances = self._c_tags[tag_type].copy()

        for tag_inst in tag_instances:
            tag_inst.detach(self)
            self._c_tags[tag_type].remove(tag_inst)

        if not self._c_tags[tag_type]:
            del self._c_tags[tag_type]

    def create(self):
        pass

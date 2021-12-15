from collections import OrderedDict


class Keywords(OrderedDict):

    """An ordered dictionary of values from any of the objects in `objects`.

    Keyword Args:
        * objects: a list of objects, usually model instances.
        * attrs: a list of attribute names to be found on any one of the objects
        * include_attrs: a subset of attribute names of `attrs` which, if not `None`,
            is used to filter the `attrs`.
    """

    def __init__(self, objects=None, attrs=None, include_attrs=None, **url_kwargs):
        super().__init__()
        if include_attrs:
            attrs = [attr for attr in attrs if attr in include_attrs]
        for attr in attrs:
            value = None
            if attr in url_kwargs:
                value = url_kwargs.get(attr)
            if not value:
                for obj in objects:
                    if value:
                        break
                    value = self.getattr(attr, obj)
                    try:
                        value = str(value.id)
                    except AttributeError:
                        pass
            self.update({attr: value or ""})

    def getattr(self, attr=None, obj=None):
        value = None
        try:
            value = getattr(obj, attr)
        except AttributeError:
            pass
        if not value:
            try:
                # assume reverse rel, remove underscore
                value = getattr(obj, attr.replace("_", ""))
            except AttributeError:
                pass
        return value

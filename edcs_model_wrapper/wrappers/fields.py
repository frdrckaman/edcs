from typing import Iterator

from django.db.models.fields.related import ForeignKey, ManyToManyField, OneToOneField
from django.db.models.fields.reverse_related import ForeignObjectRel

from ..stubs import ModelStub, ModelWrapperStub


class Fields:
    """A class that prepares model field values for use in a url.

    Fields are coerced to string or, if a foreign key, are skipped.
    """

    def __init__(self, model_obj: ModelStub) -> None:
        self.model_obj = model_obj

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model_obj={repr(self.model_obj)}))"

    def get_field_values_as_strings(self, wrapper: ModelWrapperStub) -> Iterator[tuple]:
        """Returns a generator of field name, string_value .

        If a field name is an attribute on both objects, value on wrapper_obj
        will be used, if not None.

        Skips foreign keys.
        """
        options = {}
        for field in self.model_obj._meta.get_fields():
            if (
                field.name != "id"
                and not hasattr(wrapper, field.name)
                and not isinstance(
                    field,
                    (ManyToManyField, ForeignKey, OneToOneField, ForeignObjectRel),
                )
            ):
                value = getattr(self.model_obj, field.name)
                options.update({field.name: str(value or "")})

        options.update(verbose_name=self.model_obj._meta.verbose_name)
        options.update(verbose_name_plural=self.model_obj._meta.verbose_name_plural)
        options.update(label_lower=self.model_obj._meta.label_lower)
        options.update(get_absolute_url=self.model_obj.get_absolute_url)
        if self.model_obj.id:
            str_pk = str(self.model_obj.id)
        else:
            str_pk = ""
        options.update(str_pk=str_pk)
        options.update(id=self.model_obj.id)
        for k, v in options.items():
            yield k, v

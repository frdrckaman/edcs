from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist


class SubjectRefusalModelWrapperMixin:

    refusal_model_wrapper_cls = None

    @property
    def refusal_model_cls(self):
        return django_apps.get_model(self.refusal_model_wrapper_cls.model)

    @property
    def refusal_model_obj(self):
        """Returns a refusal model instance or None."""
        try:
            model_obj = self.refusal_model_cls.objects.get(
                screening_identifier=self.object.screening_identifier
            )
        except ObjectDoesNotExist:
            model_obj = None
        return model_obj

    @property
    def refusal(self):
        """Returns a wrapped saved or unsaved refusal."""
        model_obj = self.refusal_model_obj or self.refusal_model_cls(
            screening_identifier=self.object.screening_identifier
        )
        return self.refusal_model_wrapper_cls(model_obj=model_obj)

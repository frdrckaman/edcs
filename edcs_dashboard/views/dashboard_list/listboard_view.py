from django.apps import apps as django_apps
from django.utils.translation import gettext as _


class ListboardViewError(Exception):
    pass


class BaseListboardView:
    listboard_model = None
    listboard_url = None
    cleaned_search_term = None
    context_object_name = "results"
    empty_queryset_message = _("Nothing to display.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            listboard_url=self.listboard_url
        )
        return context

    @property
    def listboard_model_cls(self):
        """Returns the listboard's model class.

        Accepts `listboard_model` as a model class or label_lower.
        """
        if not self.listboard_model:
            raise ListboardViewError(f"Listboard model not declared. Got None. See {repr(self)}")
        try:
            return django_apps.get_model(self.listboard_model)
        except (ValueError, AttributeError):
            return self.listboard_model


class ListboardView(BaseListboardView):
    urlconfig_getattr = "listboard_urls"

    @classmethod
    def get_urlname(cls):
        return cls.listboard_url

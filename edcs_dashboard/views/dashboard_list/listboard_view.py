from pprint import pprint

from django.apps import apps as django_apps
from django.utils.translation import gettext as _


class ListboardViewError(Exception):
    pass


class BaseListboardView:
    context_object_name = "results"
    empty_queryset_message = _("Nothing to display.")
    listboard_url = None  # an existing key in request.context_data
    listboard_back_url = None
    listboard_dashboard = None

    listboard_model = None  # label_lower model name or model class
    listboard_model_manager_name = "_default_manager"

    model_wrapper_cls = None
    ordering = "-created"

    # orphans = 3
    # paginate_by = 10
    # paginator_url = None  # defaults to listboard_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def object_list(self, obj):
        values = []
        data = obj.objects.all().order_by(self.ordering).values()
        if data is not None:
            for item in data:
                item['href'] = self.next_url(self.listboard_model_cls().admin_url(item['id']))
                pprint(item['href'])
                values.append(item)
        return values

    def next_url(self, href):
        return '?next='.join([href, self.listboard_dashboard])

    @property
    def listboard_model_cls(self):
        """Returns the listboard's model class.

        Accepts `listboard_model` as a model class or label_lower.
        """
        if not self.listboard_model:
            raise ListboardViewError(
                f"Listboard model not declared. Got None. See {repr(self)}"
            )
        try:
            return django_apps.get_model(self.listboard_model)
        except (ValueError, AttributeError):
            return self.listboard_model


class ListboardView(BaseListboardView):
    urlconfig_getattr = "listboard_urls"

    @classmethod
    def get_urlname(cls):
        return cls.listboard_url


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

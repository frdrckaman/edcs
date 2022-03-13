from django.apps import apps as django_apps
from django.urls import reverse
from django.utils.translation import gettext as _

from edcs_utils import age


class ListboardViewError(Exception):
    pass


class BaseListboardView:
    context_object_name = "results"
    empty_queryset_message = _("Nothing to display.")
    listboard_url = None  # an existing key in request.context_data
    listboard_back_url = None
    listboard_dashboard = None
    subjectvisit_model = None

    listboard_model = None  # label_lower model name or model class
    model_consent = None
    listboard_model_manager_name = "_default_manager"
    subject_list_dashboard = None
    paginator_url = None

    model_wrapper_cls = None
    ordering = "-created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def object_list_subject(self, obj):
        values = []
        data = obj.objects.all().order_by(self.ordering).values()
        if data is not None:
            for item in data:
                item['href'] = self.next_url_subject(item['subject_identifier'])
                if item['dob']:
                    item['age_in_years'] = age(item['dob'], item['screening_datetime']).years
                else:
                    item['age_in_years'] = '-'
                values.append(item)
        return values

    def next_url_screening(self, href, screening_identifier):
        return '?next='.join([href, self.listboard_dashboard + '&screening_identifier=' + screening_identifier])

    def next_url_subject(self, subject_identifier):
        return reverse(self.listboard_dashboard, args=[subject_identifier])

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

    @property
    def listboard_model_consent(self):
        if not self.model_consent:
            raise ListboardViewError(
                f"Listboard consent model not declared. Got None. See {repr(self)}"
            )
        try:
            return django_apps.get_model(self.model_consent)
        except (ValueError, AttributeError):
            return self.model_consent

    @property
    def listboard_model_visit(self):
        if not self.subjectvisit_model:
            raise ListboardViewError(
                f"Listboard consent model not declared. Got None. See {repr(self)}"
            )
        try:
            return django_apps.get_model(self.subjectvisit_model)
        except (ValueError, AttributeError):
            return self.subjectvisit_model

    @staticmethod
    def get_model_dict(queryset):
        return queryset.__dict__


class ListboardView(BaseListboardView):
    urlconfig_getattr = "listboard_urls"

    @classmethod
    def get_urlname(cls):
        return cls.listboard_url


class Struct:
    def __init__(self, **entries):
        self.reasons_ineligible = None
        self.eligible = None
        self.screening_identifier = None
        self.subject_consent_add_url = None
        self.consented = None
        self.subject_dashboard_url = None
        self.__dict__.update(entries)

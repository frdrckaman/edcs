from pprint import pprint

from django.views.generic import TemplateView
from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_consent.models import SubjectConsent


class SubjectDashboardView(ListboardView, TemplateView):
    listboard_url = "subject_listboard_url"
    listboard_model = "edcs_consent.subjectconsent"
    listboard_dashboard = "edcs_dashboard:enroll-dashboard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pprint(self.next_url_screening)
        context.update(
            consent_url=self.next_url_consent,
            object_list=self.get_consent_data,
        )
        return context

    @property
    def get_consent_data(self):
        consent = SubjectConsent.objects.get(subject_identifier=self.kwargs['subject'])
        return consent

    @property
    def get_consent_url(self):
        return self.listboard_model_cls().admin_url(self.get_consent_data.id)

    @property
    def next_url_consent(self):
        return '?next='.join([self.get_consent_url, self.listboard_dashboard + '&subject='
                              + self.get_consent_data.subject_identifier])

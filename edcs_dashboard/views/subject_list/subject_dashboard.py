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
        pprint(self.get_consent_data.slug)
        # context.update(
        #     object_list=self.object_list_subject(RegisteredSubject),
        # )
        return context

    @property
    def get_consent_data(self):
        consent = SubjectConsent.objects.get(subject_identifier=self.kwargs['subject'])
        return consent



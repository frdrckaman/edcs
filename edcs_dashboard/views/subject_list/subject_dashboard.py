from django.views.generic import TemplateView

from edcs_consent.models import SubjectConsent
from edcs_dashboard.view_mixins import EdcsViewMixin
from edcs_dashboard.views.dashboard_list import ListboardView


class SubjectDashboardView(EdcsViewMixin, ListboardView, TemplateView):
    listboard_url = "subject_listboard_url"
    listboard_model = "edcs_consent.subjectconsent"
    subjectvisit_model = "edcs_subject.subjectvisit"
    listboard_dashboard = "edcs_dashboard:enroll-dashboard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            consent_url=self.next_url_consent,
            consent_date=self.get_consent_date,
            object_list=self.get_consent_data,
            subject_visit=self.get_subject_visit_url,
        )
        return context

    @property
    def get_consent_data(self):
        consent = SubjectConsent.objects.get(subject_identifier=self.kwargs["subject"])
        return consent

    @property
    def get_consent_date(self):
        return self.get_consent_data.created

    @property
    def get_consent_url(self):
        return self.listboard_model_cls().admin_url(self.get_consent_data.id)

    @property
    def get_subject_visit_url(self):
        return self.listboard_model_visit().get_absolute_url()

    @property
    def next_url_consent(self):
        return "?next=".join(
            [
                self.get_consent_url,
                self.listboard_dashboard
                + "&subject="
                + self.get_consent_data.subject_identifier,
            ]
        )

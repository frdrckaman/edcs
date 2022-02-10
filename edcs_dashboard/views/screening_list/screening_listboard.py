from pprint import pprint

from django.contrib.sites.models import Site

from edcs_dashboard.view_mixins import EdcsViewMixin
from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_screening.models import SubjectScreening


class ScreeningListBoardView(EdcsViewMixin, ListboardView):
    listboard_url = "screening_listboard_url"
    listboard_model = "edcs_screening.subjectscreening"
    model_consent = "edcs_consent.subjectconsent"
    ordering = "-report_datetime"
    listboard_dashboard = "edcs_dashboard:screening_dashboard"
    subject_list_dashboard = "edcs_dashboard:enroll-dashboard"

    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # site_profile = context.get("site_profile").site_id
        # data = SubjectScreening.objects.filter(site_id=site_profile)
        # pprint(data)
        # pprint(context.get("site_profile"))
        context.update(
            subject_screening_add_url=self.next_add_screening,
            object_list=self.object_list_screening(SubjectScreening),
        )
        return context

    def get_subject_screening_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

    def get_subject_consent_add_url(self):
        return self.listboard_model_consent().get_absolute_url()

    @property
    def screening_data(self):
        return SubjectScreening.objects.all().order_by(self.ordering).values()

    @property
    def next_add_screening(self):
        nxt = '?next='.join([self.get_subject_screening_add_url(), self.listboard_dashboard])
        return nxt

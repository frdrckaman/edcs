from django.views.generic.list import ListView
from django.urls import reverse
from edcs_dashboard.view_mixins import EdcsViewMixin
from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_screening.models import SubjectScreening


class ScreeningListBoardView(EdcsViewMixin, ListboardView, ListView):
    listboard_url = "screening_listboard_url"
    listboard_model = "edcs_screening.subjectscreening"
    model_consent = "edcs_consent.subjectconsent"
    ordering = "-report_datetime"
    listboard_dashboard = "edcs_dashboard:screening_dashboard"
    subject_list_dashboard = "edcs_dashboard:enroll-dashboard"
    model = SubjectScreening
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = SubjectScreening.objects.filter(site_id=context.get('site_profile').site_id).order_by(self.ordering)
        context.update(
            subject_screening_add_url=self.next_add_screening,
            object_list=self.get_wrapped_queryset(queryset),
        )
        return context

    def get_wrapped_queryset(self, queryset):
        wrapped_objs = []
        for obj_qry in queryset:
            obj = self.get_model_dict(obj_qry)

            obj['href'] = self.next_url_screening(
                self.listboard_model_cls().admin_url(obj['id']), obj['screening_identifier'])
            obj['subject_consent_add_url'] = self.next_url_screening(
                self.listboard_model_consent().get_absolute_url(), obj['screening_identifier'])
            if obj['consented']:
                obj['subject_dashboard_url'] = reverse(self.subject_list_dashboard, args=[obj['subject_identifier']])
            else:
                obj['subject_dashboard_url'] = None
            wrapped_objs.append(obj)
        return wrapped_objs

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

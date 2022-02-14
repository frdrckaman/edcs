from django.views.generic.list import ListView

from edcs_dashboard.view_mixins import EdcsViewMixin
from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_registration.models import RegisteredSubject

from edcs_utils import age


class SubjectListBoardView(EdcsViewMixin, ListboardView, ListView):
    listboard_url = "subject_listboard_url"
    listboard_model = "edcs_registration.registeredsubject"
    model_consent = "edcs_registration.registeredsubject"
    ordering = "-created"
    listboard_dashboard = "edcs_dashboard:enroll-dashboard"
    model = RegisteredSubject

    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = RegisteredSubject.objects.filter(site_id=context.get('site_profile').site_id).order_by(self.ordering)
        context.update(
            object_list=self.get_wrapped_queryset(queryset),
        )
        return context

    def get_wrapped_queryset(self, queryset):
        wrapped_objs = []
        for obj_qry in queryset:
            obj = self.get_model_dict(obj_qry)

            obj['href'] = self.next_url_subject(obj['subject_identifier'])
            if obj['dob']:
                obj['age_in_years'] = age(obj['dob'], obj['screening_datetime']).years
            else:
                obj['age_in_years'] = '-'
            wrapped_objs.append(obj)
        return wrapped_objs

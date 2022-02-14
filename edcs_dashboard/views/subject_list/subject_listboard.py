from pprint import pprint
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

    paginate_by = 12

    def get_queryset(self):
        return RegisteredSubject.objects.all().order_by(self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            object_list=self.get_wrapped_queryset(context.get(self.context_object_name)),
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

from pprint import pprint
from django.apps import apps as django_apps
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from edcs_dashboard.views.subject_list import SubjectDashboardView
from edcs_visit_schedule.models.visit_schedule import VisitSchedule


class ListboardViewError(Exception):
    pass


class EnrollDashboardView(SubjectDashboardView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/enroll_dashboard.html"
    # listboard_model = "edcs_appointment.appointment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            appointments=VisitSchedule.objects.all(),
        )
        # pprint(self.listboard_model_cls().get_absolute_url())
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edcs_appointment.models import Appointment
from edcs_crf.crfs import enrollment_crf, followup_crf
from edcs_dashboard.views.subject_list import CrfListBoardView


class CrfListView(CrfListBoardView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/crf_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            crfs=self.get_crf_data,
        )
        return context

    @property
    def get_crf_data(self):
        return followup_crf if int(self.get_appt_data) > 1 else enrollment_crf

    @property
    def get_appt_data(self):
        return Appointment.objects.get(id=self.kwargs["appointment"]).timepoint

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

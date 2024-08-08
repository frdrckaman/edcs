from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edcs_appointment.models import Appointment
from edcs_crf.crfs import enrollment_crf, followup_crf
from edcs_dashboard.views.subject_list import CrfListBoardView
from edcs_subject.models import Genotypic, GenotypicCancerProfile, SubjectVisit


class CrfListView(CrfListBoardView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/crf_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        s_visit = SubjectVisit.objects.get(appointment=self.kwargs["appointment"])
        genotypics = Genotypic.objects.filter(subject_identifier=s_visit.subject_identifier)
        context.update(
            genotypics=genotypics,
            crfs=self.get_crf_data,
        )
        return context

    @property
    def get_crf_data(self):
        return followup_crf if int(self.get_appt_data) > 1 else enrollment_crf

    @property
    def get_appt_data(self):
        return Appointment.objects.get(id=self.kwargs["appointment"]).timepoint

    # @property
    # def get_genotypic_data(self):
    #     return GenotypicCancerProfile.objects.get(subject_identifier=self.kwargs["subject"])

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

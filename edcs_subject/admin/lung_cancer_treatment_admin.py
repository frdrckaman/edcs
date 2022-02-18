from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import LungCancerTreatmentForm
from ..models import LungCancerTreatment


@admin.register(LungCancerTreatment, site=edcs_subject_admin)
class LungCancerTreatmentAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = LungCancerTreatmentForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "LUNG CANCER TREATMENT",
            {
                "fields": (
                    "lung_cancer_stage",
                    "date_start_treatment",
                    "treatment",
                    "treatment_other",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "lung_cancer_stage",
        "date_start_treatment",
        "treatment",
        "treatment_other",
        "created",
    )

    list_filter = (
        "report_datetime",
        "lung_cancer_stage",
        "date_start_treatment",
        "treatment",
        "treatment_other",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "lung_cancer_stage": admin.VERTICAL,
        "treatment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(FollowUp, site=edcs_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = FollowUpForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "TEST ORDERED",
            {
                "fields": (
                    "test_ordered",
                    "test_ordered_other",
                    "test_ordered_result",
                    "hiv_status",
                    "viral_load_cd4_off",
                    "current_viral_load",
                    "current_cd4_count",
                    "hiv_genotype",
                ),
            },
        ),
        (
            "PATIENT STATUS",
            {
                "fields": (
                    "patient_visit_status",
                    "respond_treatment",
                    "treatment_change",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hiv_status",
        "current_viral_load",
        "current_cd4_count",
        "patient_visit_status",
    )

    list_filter = (
        "report_datetime",
        "patient_visit_status",
        "hiv_status",
        "hiv_genotype",
    )

    search_fields = ("report_datetime", "subject_visit")

    radio_fields = {
        "test_ordered": admin.VERTICAL,
        "hiv_status": admin.VERTICAL,
        "hiv_genotype": admin.VERTICAL,
        "patient_visit_status": admin.VERTICAL,
        "respond_treatment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

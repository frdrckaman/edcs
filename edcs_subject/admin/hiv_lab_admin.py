from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import HivLabInvestigationForm
from ..models import HivLabInvestigation


@admin.register(HivLabInvestigation, site=edcs_subject_admin)
class HivLabInvestigationAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = HivLabInvestigationForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV LABORATORY INVESTIGATIONS",
            {
                "fields": (
                    "hiv_status",
                    "baseline_cd4",
                    "baseline_viral_load",
                    "hiv_stage",
                    "hiv_subtype_done",
                    "hiv_subtype",
                    "drug_resistance_testing_done",
                    "drug_resistance",
                    "treatment_other",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "baseline_cd4",
        "baseline_viral_load",
        "hiv_stage",
        "hiv_subtype_done",
        "hiv_subtype",
    )

    list_filter = (
        "report_datetime",
        "report_datetime",
        "baseline_cd4",
        "baseline_viral_load",
        "hiv_stage",
        "hiv_subtype_done",
        "hiv_subtype",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "hiv_status": admin.VERTICAL,
        "hiv_stage": admin.VERTICAL,
        "hiv_subtype_done": admin.VERTICAL,
        "hiv_subtype": admin.VERTICAL,
        "drug_resistance_testing_done": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

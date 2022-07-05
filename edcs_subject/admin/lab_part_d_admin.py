from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import LabPartDForm
from ..models.lab_part_d import LabPartD
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(LabPartD, site=edcs_subject_admin)
class LabPartDAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = LabPartDForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "LAB PART D",
            {
                "fields": (
                    "hiv_dna_pcr",
                    "hiv_subtype",
                    "somatic_mutations",
                    "dna_methylation",
                    "hiv_drug_resistance_test",
                    "hiv_drug_resistance_other",
                    "hiv_current_regimen",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hiv_dna_pcr",
        "dna_methylation",
        "hiv_current_regimen",
    )

    list_filter = (
        "report_datetime",
        "hiv_dna_pcr",
        "hiv_subtype",
    )

    search_fields = (
        "report_datetime",
        "hiv_dna_pcr",
        "hiv_subtype",
        "dna_methylation",
    )

    filter_horizontal = [
        "hiv_subtype",
        "somatic_mutations",
    ]

    radio_fields = {
        "hiv_dna_pcr": admin.VERTICAL,
        "hiv_drug_resistance_test": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

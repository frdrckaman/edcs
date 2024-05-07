from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin

# from ..forms import HivLabInvestigationForm
from ..models import GenotypicCancerProfile
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(GenotypicCancerProfile, site=edcs_subject_admin)
class GenotypicCancerProfileAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    # form = HivLabInvestigationForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "GENOTYPIC CANCER PROFILE",
            {
                "fields": (
                    "sample_type",
                    "date_received",
                    "cancer_type",
                    "genomic_alteration",
                    "allele_frequency",
                    "variant_class",
                    "coverage",
                    "biomarker_this_cancer",
                    "biomarker_other_cancer",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "sample_type",
        "date_received",
        "genomic_alteration",
        "allele_frequency",
        "variant_class",
        "coverage",
    )

    list_filter = (
        "report_datetime",
        "sample_type",
        "date_received",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "crf_status": admin.VERTICAL,
    }

from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import LungCancerLabInvestigation


@admin.register(LungCancerLabInvestigation, site=edcs_subject_admin)
class LungCancerLabInvestigationAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "MUTATION ANALYSIS",
            {
                "fields": (
                    "biopsy_tissues_mutation",
                    "mutation_detected",
                ),
            },
        ),
        (
            "DNA METYLATION AGE ANALYSIS",
            {
                "fields": (
                    "dna_methylation_age",
                    "dna_methylation_result",
                ),
            },
        ),
        (
            "RADIOLOGY INVESTIGATIONS",
            {
                "fields": (
                    "brock_score",
                    "lungrads_score",
                    "luniris_score",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "biopsy_tissues_mutation",
        "dna_methylation_age",
        "brock_score",
        "lungrads_score",
        "luniris_score",
    )

    list_filter = (
        "report_datetime",
        "biopsy_tissues_mutation",
        "dna_methylation_age",
        "brock_score",
        "lungrads_score",
        "luniris_score",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "biopsy_tissues_mutation": admin.VERTICAL,
        "dna_methylation_age": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

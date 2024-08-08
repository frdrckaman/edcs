from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import GenotypicForm
from ..modeladmin_mixins import SubjectAdminMethodsMixin

# from ..forms import HivLabInvestigationForm
from ..models import Genotypic, GenotypicCancerProfile
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(Genotypic, site=edcs_subject_admin)
class GenotypicAdmin(SubjectAdminMethodsMixin, SimpleHistoryAdmin):

    form = GenotypicForm

    fieldsets = (
        (
            "GENOTYPIC CANCER PROFILE",
            {
                "fields": (
                    "subject_identifier",
                    "report_datetime",
                    "assay_status",
                    "oncomine_variant",
                    "gene",
                    "genotype",
                    "amino_acid_change",
                    "coverage",
                    "allele_frequency",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "genotype",
        "amino_acid_change",
        "coverage",
        "allele_frequency",
    )

    list_filter = ("report_datetime",)

    search_fields = ("report_datetime",)

    filter_horizontal = [
        "oncomine_variant",
    ]

    radio_fields = {
        "assay_status": admin.VERTICAL,
    }

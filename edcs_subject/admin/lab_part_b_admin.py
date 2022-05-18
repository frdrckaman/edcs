from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import LabPartBForm
from ..models import LabPartB
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(LabPartB, site=edcs_subject_admin)
class LabPartBAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = LabPartBForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "LAB PART B",
            {
                "fields": (
                    "side_biopsy_taken",
                    "location_site",
                    "nature_of_specimen",
                    "xray_findings",
                    "ct_findings",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "side_biopsy_taken",
        "location_site",
        "nature_of_specimen",
        "xray_findings",
        "ct_findings",
    )

    list_filter = (
        "report_datetime",
        "side_biopsy_taken",
        "location_site",
    )

    search_fields = (
        "report_datetime",
        "side_biopsy_taken",
        "location_site",
    )

    radio_fields = {
        "side_biopsy_taken": admin.VERTICAL,
        "location_site": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

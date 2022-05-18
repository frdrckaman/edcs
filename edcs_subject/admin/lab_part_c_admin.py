from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import LabPartCForm
from ..models import LabPartC
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(LabPartC, site=edcs_subject_admin)
class LabPartCAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = LabPartCForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "LAB PART C",
            {
                "fields": (
                    "histological_dx",
                    "measurements",
                    "consistency",
                    "color",
                    "microscopic_findings",
                    "immunohistochemistry",
                    "histochemistry",
                    "type_lung_ca",
                    "non_small_cell",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "immunohistochemistry",
        "histochemistry",
        "type_lung_ca",
        "non_small_cell",
        "measurements",
    )

    list_filter = (
        "report_datetime",
        "immunohistochemistry",
        "histochemistry",
        "type_lung_ca",
        "non_small_cell",
    )

    search_fields = (
        "report_datetime",
        "immunohistochemistry",
        "histochemistry",
        "type_lung_ca",
        "non_small_cell",
    )

    radio_fields = {
        "immunohistochemistry": admin.VERTICAL,
        "histochemistry": admin.VERTICAL,
        "type_lung_ca": admin.VERTICAL,
        "non_small_cell": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

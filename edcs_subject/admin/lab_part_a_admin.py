from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import LabPartAForm
from ..models import LabPartA
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(LabPartA, site=edcs_subject_admin)
class LabPartAAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = LabPartAForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "LAB PART A",
            {
                "fields": (
                    "hiv_rapid_test",
                    "type_tb_test",
                    "type_tb_test_other",
                    "tb_test_result",
                    "baseline_cd4_counts",
                    "baseline_viral_load",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hiv_rapid_test",
        "type_tb_test",
        "tb_test_result",
    )

    list_filter = (
        "report_datetime",
        "hiv_rapid_test",
        "type_tb_test",
        "tb_test_result",
    )

    search_fields = (
        "report_datetime",
        "hiv_rapid_test",
        "type_tb_test",
        "tb_test_result",
    )

    radio_fields = {
        "hiv_rapid_test": admin.VERTICAL,
        "type_tb_test": admin.VERTICAL,
        "tb_test_result": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

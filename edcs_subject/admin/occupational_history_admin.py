from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import OccupationalHistoryForm
from ..models import OccupationalHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(OccupationalHistory, site=edcs_subject_admin)
class OccupationalHistoryAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = OccupationalHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "OCCUPATIONAL HISTORY",
            {
                "fields": (
                    "history_working_industries",
                    "industries_worked",
                    "industries_worked_other",
                    "history_working_mines",
                    "how_long_work_mine",
                    "activities_expose_to_smoke",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "history_working_industries",
        "history_working_mines",
        "how_long_work_mine",
        "activities_expose_to_smoke",
        "created",
    )

    list_filter = (
        "report_datetime",
        "history_working_industries",
        "history_working_mines",
        "how_long_work_mine",
        "activities_expose_to_smoke",
    )

    search_fields = ("report_datetime",)

    filter_horizontal = [
        "industries_worked",
    ]

    radio_fields = {
        "history_working_industries": admin.VERTICAL,
        "history_working_mines": admin.VERTICAL,
        "how_long_work_mine": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

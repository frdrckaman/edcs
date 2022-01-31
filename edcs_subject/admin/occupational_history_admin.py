from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import OccupationalHistory


@admin.register(OccupationalHistory, site=edcs_subject_admin)
class OccupationalHistoryAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "OCCUPATIONAL HISTORY",
            {
                "fields": (
                    "history_working_industries",
                    "industries_worked_on",
                    "history_working_mines",
                    "how_long_work_mine",
                    "activities_expose_to_smoke",
                ),
            },
        ),

        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "history_working_industries",
        "industries_worked_on",
        "history_working_mines",
        "how_long_work_mine",
        "activities_expose_to_smoke",
        "created",
    )

    list_filter = (
        "report_datetime",
        "history_working_industries",
        "industries_worked_on",
        "history_working_mines",
        "how_long_work_mine",
        "activities_expose_to_smoke",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "history_working_industries": admin.VERTICAL,
        "industries_worked_on": admin.VERTICAL,
        "history_working_mines": admin.VERTICAL,
        "how_long_work_mine": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import PreAirQualityForm
from ..models.pre_air_quality import PreAirQuality
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PreAirQuality, site=edcs_subject_admin)
class PreAirQualityAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = PreAirQualityForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Household Air Monitoring",
            {
                "fields": (
                    "monitor_start_date",
                    "selected_air_monitor",
                    "household_num",
                    "gender",
                    "total_num_rooms",
                    "total_num_windows",
                    "cooking_done",
                    "cooking_area",
                    "cooking_done_outside",
                    "cooking_fuel",
                    "cooking_fuel_other",
                    "cooking_fuel_duration",
                    "previously_used_cooking_fuel",
                    "previously_cooking_fuel",
                    "previously_cooking_fuel_other",
                    "previously_cooking_fuel_duration",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "monitor_start_date",
        "selected_air_monitor",
        "gender",
        "cooking_fuel",
        "previously_used_cooking_fuel",
    )

    list_filter = (
        "report_datetime",
        "monitor_start_date",
        "selected_air_monitor",
        "gender",
        "cooking_fuel",
    )

    search_fields = (
        "report_datetime",
        "subject_visit",
        "monitor_start_date",
        "selected_air_monitor",
    )

    filter_horizontal = [
        "cooking_done",
        "cooking_area",
    ]

    radio_fields = {
        "selected_air_monitor": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "cooking_fuel": admin.VERTICAL,
        "previously_used_cooking_fuel": admin.VERTICAL,
        "previously_cooking_fuel": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

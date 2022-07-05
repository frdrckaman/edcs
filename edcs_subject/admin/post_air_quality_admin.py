from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import PostAirQualityForm
from ..models.post_air_quality import PostAirQuality
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(PostAirQuality, site=edcs_subject_admin)
class PostAirQualityAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = PostAirQualityForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "Household activities during air pollution monitoring",
            {
                "fields": (
                    "monitor_end_date",
                    "air_monitor_problem",
                    "air_monitor_problem_list",
                ),
            },
        ),
        (
            "Household cooking",
            {
                "fields": (
                    "cooking_fuel_used",
                    "cooking_fuel_used_other",
                    "cooking_fuel_used_duration",
                    "other_cooking_fuel",
                    "other_cooking_fuel_other",
                    "other_cooking_fuel_duration",
                    "solid_fuel",
                    "solid_fuel_other",
                ),
            },
        ),
        (
            "Household heating",
            {
                "fields": (
                    "primary_fuel_heating",
                    "primary_fuel_heating_other",
                    "primary_fuel_heating_duration",
                ),
            },
        ),
        (
            "Tobacco Smoke",
            {
                "fields": (
                    "smoke_inside",
                    "smoke_inside_duration",
                ),
            },
        ),
        ("Air Pollution Readings", {"fields": ("air_pollution_monitor_reading",)}),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "monitor_end_date",
        "air_monitor_problem",
        "cooking_fuel_used",
    )

    list_filter = (
        "report_datetime",
        "monitor_end_date",
        "air_monitor_problem",
        "cooking_fuel_used",
    )

    search_fields = (
        "report_datetime",
        "monitor_end_date",
        "subject_visit",
    )

    filter_horizontal = [
        "air_monitor_problem_list",
        "other_cooking_fuel",
        "solid_fuel",
    ]

    radio_fields = {
        "air_monitor_problem": admin.VERTICAL,
        "cooking_fuel_used": admin.VERTICAL,
        "primary_fuel_heating": admin.VERTICAL,
        "smoke_inside": admin.VERTICAL,
        "smoke_inside_duration": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

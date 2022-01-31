from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin
from edcs_crf.admin import crf_status_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import AirPollutionFollowUp


@admin.register(AirPollutionFollowUp, site=edcs_subject_admin)
class AirPollutionFollowUpAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "AIR POLLUTION FOLLOW UP ",
            {
                "fields": (
                    "hour_wear_device",
                    "who_had_illness",
                    "fuel_before_changing",
                    "pollution_readings",
                    "gps_coordinates",
                    "distance_health_facility",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hour_wear_device",
        "who_had_illness",
        "fuel_before_changing",
        "pollution_readings",
        "gps_coordinates",
        "distance_health_facility",
        "created",
    )

    list_filter = (
        "report_datetime",
        "hour_wear_device",
        "who_had_illness",
        "fuel_before_changing",
        "pollution_readings",
        "gps_coordinates",
        "distance_health_facility",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "who_had_illness": admin.VERTICAL,
        "fuel_before_changing": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

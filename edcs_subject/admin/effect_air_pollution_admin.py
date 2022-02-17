from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import EffectAirPollutionForm
from ..models import EffectAirPollution


@admin.register(EffectAirPollution, site=edcs_subject_admin)
class EffectAirPollutionAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = EffectAirPollutionForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "EFFECT OF AIR POLLUTION",
            {
                "fields": (
                    "family_member_sickness",
                    "who_had_illness",
                    "fuel_before_changing",
                    "variation_btn_fuel",
                    "influence_variation_btn_fuel",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "family_member_sickness",
        "who_had_illness",
        "fuel_before_changing",
        "variation_btn_fuel",
        "influence_variation_btn_fuel",
    )

    list_filter = (
        "report_datetime",
        "family_member_sickness",
        "who_had_illness",
        "fuel_before_changing",
        "variation_btn_fuel",
        "influence_variation_btn_fuel",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "family_member_sickness": admin.VERTICAL,
        "who_had_illness": admin.VERTICAL,
        "variation_btn_fuel": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

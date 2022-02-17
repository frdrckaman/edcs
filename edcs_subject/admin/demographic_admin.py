from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import DemographicCharacteristicForm
from ..models import DemographicCharacteristic


@admin.register(DemographicCharacteristic, site=edcs_subject_admin)
class DemographicCharacteristicAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = DemographicCharacteristicForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "DEMOGRAPHIC CHARACTERISTIC",
            {
                "fields": (
                    "martial_status",
                    "education",
                    "education_other",
                    "occupation",
                    "occupation_other",
                ),
            },
        ),
        (
            "SOCIAL-ECONOMIC CHARACTERISTICS",
            {
                "fields": (
                    "electricity",
                    "television",
                    "radio",
                    "an_iron",
                    "bank_account",
                    "material_build_floor",
                    "material_build_floor_other",
                    "material_build_walls",
                    "material_build_walls_other",
                    "material_build_roof",
                    "material_build_roof_other",
                    "use_in_cooking",
                    "use_in_cooking_other",
                    "main_power_source",
                    "main_power_source_other",
                    "household_monthly_income",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "martial_status",
        "education",
        "occupation",
        "electricity",
        "television",
        "bank_account",
        "use_in_cooking",
        "created",
    )

    list_filter = (
        "martial_status",
        "education",
        "occupation",
        "electricity",
        "television",
        "bank_account",
        "use_in_cooking",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "martial_status": admin.VERTICAL,
        "education": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "electricity": admin.VERTICAL,
        "television": admin.VERTICAL,
        "radio": admin.VERTICAL,
        "an_iron": admin.VERTICAL,
        "bank_account": admin.VERTICAL,
        "material_build_floor": admin.VERTICAL,
        "material_build_walls": admin.VERTICAL,
        "material_build_roof": admin.VERTICAL,
        "use_in_cooking": admin.VERTICAL,
        "main_power_source": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

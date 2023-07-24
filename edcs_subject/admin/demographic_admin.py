from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import DemographicCharacteristicForm
from ..models import DemographicCharacteristic
from .modeladmin_mixins import CrfModelAdminMixin


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
                    "occupation_details",
                    "occupation_duration",
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
        "created",
    )

    list_filter = (
        "martial_status",
        "education",
        "occupation",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "martial_status": admin.VERTICAL,
        "education": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import AlcoholTobaccoUse


@admin.register(AlcoholTobaccoUse, site=edcs_subject_admin)
class AlcoholTobaccoUseAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "TOBACCO",
            {
                "fields": (
                    "smoke_tobacco",
                    "tobacco_product",
                    "date_start_smoking",
                    "smoking_frequency",
                    "smoking_frequency_other",
                    "no_tobacco_product_smoked",
                    "age_start_smoking",
                    "age_stop_smoking",
                    "someone_else_smoke",
                    "smoke_inside_house",
                    "smoke_inside_house_other",
                ),
            },
        ),
        (
            "ALCOHOL",
            {
                "fields": (
                    "consume_alcohol",
                    "alcohol_consumption_frequency",
                    "alcohol_consumption_frequency_other",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "smoke_tobacco",
        "age_start_smoking",
        "smoke_inside_house",
        "consume_alcohol",
        "alcohol_consumption_frequency",
    )

    list_filter = (
        "tobacco_product",
        "smoking_frequency",
        "smoking_frequency_other",
        "no_tobacco_product_smoked",
        "age_start_smoking",
        "age_stop_smoking",
        "someone_else_smoke",
        "smoke_inside_house",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "smoke_tobacco": admin.VERTICAL,
        "tobacco_product": admin.VERTICAL,
        "smoking_frequency": admin.VERTICAL,
        "someone_else_smoke": admin.VERTICAL,
        "smoke_inside_house": admin.VERTICAL,
        "consume_alcohol": admin.VERTICAL,
        "alcohol_consumption_frequency": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

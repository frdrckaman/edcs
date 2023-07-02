from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import AlcoholTobaccoUseForm
from ..models import AlcoholTobaccoUse
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(AlcoholTobaccoUse, site=edcs_subject_admin)
class AlcoholTobaccoUseAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = AlcoholTobaccoUseForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "TOBACCO",
            {
                "fields": (
                    "smoke_chew_tobacco",
                    "tobacco_products",
                    "tobacco_products_other",
                    "date_start_smoking",
                    # "smoking_frequency",
                    # "smoking_frequency_other",
                    "smoking_frequency_cigarettes",
                    "smoking_frequency_other_cigarettes",
                    "smoking_frequency_cigars",
                    "smoking_frequency_other_cigars",
                    "smoking_frequency_shisha",
                    "smoking_frequency_other_shisha",
                    "smoking_frequency_pipes",
                    "smoking_frequency_other_pipes",
                    "no_cigarettes_smoked",
                    "no_cigars_smoked",
                    "no_shisha_smoked",
                    "no_pipe_smoked",
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
        "age_start_smoking",
        "smoke_inside_house",
        "consume_alcohol",
        "alcohol_consumption_frequency",
    )

    list_filter = (
        # "smoking_frequency",
        # "smoking_frequency_other",
        "no_tobacco_product_smoked",
        "age_start_smoking",
        "age_stop_smoking",
        "someone_else_smoke",
        "smoke_inside_house",
    )

    search_fields = ("report_datetime",)

    filter_horizontal = [
        "smoke_chew_tobacco",
        "tobacco_products",
    ]

    radio_fields = {
        # "smoking_frequency": admin.VERTICAL,
        "smoking_frequency_cigarettes": admin.VERTICAL,
        "smoking_frequency_cigars": admin.VERTICAL,
        "smoking_frequency_shisha": admin.VERTICAL,
        "smoking_frequency_pipes": admin.VERTICAL,
        "someone_else_smoke": admin.VERTICAL,
        "smoke_inside_house": admin.VERTICAL,
        "consume_alcohol": admin.VERTICAL,
        "alcohol_consumption_frequency": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import CookingFuelForm
from ..models import CookingFuel


@admin.register(CookingFuel, site=edcs_subject_admin)
class CookingFuelAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = CookingFuelForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "COOKING FUEL",
            {
                "fields": (
                    "main_use_cooking",
                    "main_use_cooking_other",
                    "main_reason_use",
                    "cooking_done",
                    "cooking_done_other",
                    "no_cooking_household",
                    "sleep_where_cook",
                    "use_wood",
                    "use_wood_per_month",
                    "use_kerosene",
                    "use_kerosene_per_month",
                    "use_charcoal",
                    "use_charcoal_per_month",
                    "use_coal",
                    "use_coal_per_month",
                    "use_straw",
                    "use_straw_per_month",
                    "use_electricity",
                    "use_electricity_per_month",
                    "use_biogas",
                    "use_biogas_per_month",
                    "use_dung",
                    "use_dung_per_month",
                    "use_paper",
                    "use_paper_per_month",
                    "use_polythene",
                    "use_polythene_per_month",
                    "use_burn_crops",
                    "distance_from_neighbor",
                    "neighbor_use_cooking",
                    "neighbor_use_cooking_other",
                    "smoke_from_neighbor",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "main_use_cooking",
        "cooking_done",
        "use_wood",
        "use_kerosene",
        "use_charcoal",
        "use_coal",
        "use_straw",
        "use_electricity",
        "use_biogas",
        "use_dung",
        "use_paper",
        "use_polythene",
        "use_burn_crops",
    )

    list_filter = (
        "report_datetime",
        "main_use_cooking",
        "cooking_done",
        "use_wood",
        "use_kerosene",
        "use_charcoal",
        "use_coal",
        "use_straw",
        "use_electricity",
        "use_biogas",
        "use_dung",
        "use_paper",
        "use_polythene",
        "use_burn_crops",
        "distance_from_neighbor",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "main_use_cooking": admin.VERTICAL,
        "main_reason_use": admin.VERTICAL,
        "cooking_done": admin.VERTICAL,
        "sleep_where_cook": admin.VERTICAL,
        "use_wood": admin.VERTICAL,
        "use_wood_per_month": admin.VERTICAL,
        "use_kerosene": admin.VERTICAL,
        "use_kerosene_per_month": admin.VERTICAL,
        "use_charcoal": admin.VERTICAL,
        "use_charcoal_per_month": admin.VERTICAL,
        "use_coal": admin.VERTICAL,
        "use_coal_per_month": admin.VERTICAL,
        "use_straw": admin.VERTICAL,
        "use_straw_per_month": admin.VERTICAL,
        "use_electricity": admin.VERTICAL,
        "use_electricity_per_month": admin.VERTICAL,
        "use_biogas": admin.VERTICAL,
        "use_biogas_per_month": admin.VERTICAL,
        "use_dung": admin.VERTICAL,
        "use_dung_per_month": admin.VERTICAL,
        "use_paper": admin.VERTICAL,
        "use_paper_per_month": admin.VERTICAL,
        "use_polythene": admin.VERTICAL,
        "use_polythene_per_month": admin.VERTICAL,
        "use_burn_crops": admin.VERTICAL,
        "neighbor_use_cooking": admin.VERTICAL,
        "smoke_from_neighbor": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }
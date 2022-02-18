from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import HouseKitchenSurroundingForm
from ..models import HouseKitchenSurrounding


@admin.register(HouseKitchenSurrounding, site=edcs_subject_admin)
class HouseKitchenSurroundingAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = HouseKitchenSurroundingForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HOUSE SURROUNDINGS",
            {
                "fields": (
                    "material_floor",
                    "material_roof",
                    "material_interior_wall",
                    "material_exterior_wall",
                    "inside_swept",
                ),
            },
        ),
        (
            "KITCHEN SURROUNDINGS",
            {
                "fields": (
                    "material_kitchen_floor",
                    "material_kitchen_roof",
                    "material_interior_wall_kitchen",
                    "material_exterior_wall_kitchen",
                    "kitchen_swept",
                    "no_kitchen_window",
                    "no_kitchen_door",
                    "kitchen_chimney",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "material_floor",
        "material_roof",
        "material_kitchen_floor",
        "material_kitchen_roof",
        "inside_swept",
        "kitchen_swept",
        "kitchen_chimney",
        "created",
    )

    list_filter = (
        "report_datetime",
        "material_floor",
        "material_roof",
        "material_kitchen_floor",
        "material_kitchen_roof",
        "inside_swept",
        "kitchen_swept",
        "kitchen_chimney",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "material_floor": admin.VERTICAL,
        "material_roof": admin.VERTICAL,
        "material_interior_wall": admin.VERTICAL,
        "material_exterior_wall": admin.VERTICAL,
        "inside_swept": admin.VERTICAL,
        "material_kitchen_floor": admin.VERTICAL,
        "material_kitchen_roof": admin.VERTICAL,
        "material_interior_wall_kitchen": admin.VERTICAL,
        "material_exterior_wall_kitchen": admin.VERTICAL,
        "kitchen_swept": admin.VERTICAL,
        "kitchen_chimney": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

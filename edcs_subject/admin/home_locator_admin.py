from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..forms import HomeLocatorForm
from ..models import HomeLocator


@admin.register(HomeLocator, site=edcs_subject_admin)
class HomeLocatorFormAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = HomeLocatorForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HOME LOCATOR",
            {
                "fields": (
                    "ward",
                    "village",
                    "street",
                    "Kitongoji",
                    "Kitongoji_leader",
                    "nearest_church_mosque",
                    "nearest_healthcare_facility",
                    "famous_person",
                    "famous_thing",
                    "patient_phone_number",
                    "member_phone_number",
                    "close_relatives_phone_number",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "ward",
        "village",
        "street",
        "Kitongoji",
        "famous_thing",
        "patient_phone_number",
    )

    list_filter = (
        "ward",
        "village",
        "street",
        "Kitongoji",
        "famous_thing",
        "patient_phone_number",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "crf_status": admin.VERTICAL,
    }

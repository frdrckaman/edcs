from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..models import HomeLocatorForm


@admin.register(HomeLocatorForm, site=edcs_subject_admin)
class HomeLocatorFormAdmin(SimpleHistoryAdmin):
    fieldsets = (
        [
            None,
            {
                "fields": (
                    "report_datetime",
                ),
            },
         ],
        [
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
        ],

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

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

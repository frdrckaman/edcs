from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import SignSymptomLungCancer


@admin.register(SignSymptomLungCancer, site=edcs_subject_admin)
class SignSymptomLungCancerAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "SIGNS AND SYMPTOMS OF LUNG CANCER",
            {
                "fields": (
                    "what_brought_hospital",
                    "symptoms_how_long",
                    "characterize_symptoms",
                    "family_member_same_symptoms",
                    "family_member_relationship",
                    "family_member_dx_cancer",
                    "time_take_referred_cancer_facilities",
                    "investigations_ordered",
                    "non_investigations_ordered",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "what_brought_hospital",
        "symptoms_how_long",
        "characterize_symptoms",
        "family_member_same_symptoms",
        "family_member_relationship",
        "family_member_dx_cancer",
        "time_take_referred_cancer_facilities",
        "investigations_ordered",
    )

    list_filter = (
        "report_datetime",
        "what_brought_hospital",
        "symptoms_how_long",
        "characterize_symptoms",
        "family_member_same_symptoms",
        "family_member_relationship",
        "family_member_dx_cancer",
        "time_take_referred_cancer_facilities",
        "investigations_ordered",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "what_brought_hospital": admin.VERTICAL,
        "symptoms_how_long": admin.VERTICAL,
        "characterize_symptoms": admin.VERTICAL,
        "family_member_same_symptoms": admin.VERTICAL,
        "family_member_relationship": admin.VERTICAL,
        "family_member_dx_cancer": admin.VERTICAL,
        "investigations_ordered": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

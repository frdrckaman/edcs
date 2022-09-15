from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import SignSymptomLungCancerForm
from ..models import SignSymptomLungCancer
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(SignSymptomLungCancer, site=edcs_subject_admin)
class SignSymptomLungCancerAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = SignSymptomLungCancerForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "SIGNS AND SYMPTOMS OF LUNG CANCER",
            {
                "fields": (
                    "what_brought_hospital",
                    "what_brought_hospital_other",
                    "symptoms_how_long",
                    "symptoms_greater_than_6months",
                    "characterize_symptoms",
                    "characterize_symptoms_other",
                    "family_member_same_symptoms",
                    "family_member_relationship",
                    "family_member_relationship_other",
                    "chest_radiation",
                    "no_chest_radiation",
                    "time_take_referred_cancer_facilities",
                    "investigations_ordered_nw",
                    "investigations_ordered_other",
                    "non_investigations_ordered",
                    "lung_cancer_dx",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "symptoms_how_long",
        "characterize_symptoms",
        "family_member_same_symptoms",
        "family_member_relationship",
        "time_take_referred_cancer_facilities",
    )

    list_filter = (
        "report_datetime",
        "symptoms_how_long",
        "characterize_symptoms",
        "family_member_same_symptoms",
        "family_member_relationship",
        "time_take_referred_cancer_facilities",
    )

    search_fields = ("report_datetime",)

    filter_horizontal = ["what_brought_hospital", "investigations_ordered_nw"]

    radio_fields = {
        "symptoms_how_long": admin.VERTICAL,
        "characterize_symptoms": admin.VERTICAL,
        "family_member_same_symptoms": admin.VERTICAL,
        "family_member_relationship": admin.VERTICAL,
        "chest_radiation": admin.VERTICAL,
        "lung_cancer_dx": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

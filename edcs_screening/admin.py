from django.contrib import admin
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.model_admin_form_auto_number_mixin import ModelAdminFormAutoNumberMixin

from .admin_site import edcs_screening_admin
from .models import SubjectScreening


@admin.register(SubjectScreening, site=edcs_screening_admin)
class SubjectScreeningAdmin(ModelAdminFormAutoNumberMixin, SimpleHistoryAdmin):
    fieldsets = (
        [
            None,
            {
                "fields": (
                    "report_datetime",
                    "screening_consent",
                ),
            },
         ],
        [
            "Demographics",
            {
                "fields": (
                    "region",
                    "district",
                    "patient_know_dob",
                    "age_in_years",
                    "gender",
                    "hospital_id",
                    "initials"
                ),
            },
        ],
        [
            "Criteria",
            {
                "fields": (
                    "tb_diagnosis",
                    "above_eighteen",
                    "lung_cancer_suspect",
                    "cough",
                    "long_standing_cough",
                    "cough_blood",
                    "chest_infections",
                    "chest_pain",
                    "persistent_breathlessness",
                    "persistent_tiredness",
                    "wheezing",
                    "shortness_of_breath",
                    "weight_loss",
                    "abnormal_chest_xrays",
                    "non_resolving_infection",
                    "malignancy",
                    "diagnosed_lung_cancer",
                ),
            },
        ],
        audit_fieldset_tuple,
    )

    list_display = (
        "screening_identifier",
        "demographics",
        "report_datetime",
        "user_created",
        "created",
    )

    list_filter = (
        "report_datetime",
        "gender",
    )

    search_fields = (
        "screening_identifier",
    )

    radio_fields = {
        "screening_consent": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "patient_know_dob": admin.VERTICAL,
        "tb_diagnosis": admin.VERTICAL,
        "above_eighteen": admin.VERTICAL,
        "lung_cancer_suspect": admin.VERTICAL,
        "cough": admin.VERTICAL,
        "long_standing_cough": admin.VERTICAL,
        "cough_blood": admin.VERTICAL,
        "chest_infections": admin.VERTICAL,
        "chest_pain": admin.VERTICAL,
        "persistent_breathlessness": admin.VERTICAL,
        "persistent_tiredness": admin.VERTICAL,
        "wheezing": admin.VERTICAL,
        "shortness_of_breath": admin.VERTICAL,
        "weight_loss": admin.VERTICAL,
        "abnormal_chest_xrays": admin.VERTICAL,
        "non_resolving_infection": admin.VERTICAL,
        "malignancy": admin.VERTICAL,
        "diagnosed_lung_cancer": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

    def demographics(self, obj=None):
        return mark_safe(
            f"{obj.get_gender_display()} {obj.age_in_years}yrs "
        )

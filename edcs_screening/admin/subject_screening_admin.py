from django.contrib import admin, messages
from django.shortcuts import redirect
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.dashboard import ModelAdminDashboardMixin
from edcs_screening.admin_site import edcs_screening_admin
from edcs_screening.forms.subject_screening_form import SubjectScreeningForm
from edcs_screening.models import SubjectScreening


@admin.register(SubjectScreening, site=edcs_screening_admin)
class SubjectScreeningAdmin(ModelAdminDashboardMixin, SimpleHistoryAdmin):
    form = SubjectScreeningForm
    fieldsets = (
        [
            None,
            {
                "fields": (
                    "report_datetime",
                    "screening_consent",
                    "clinic_type",
                    "patient_category",
                ),
            },
        ],
        [
            "Demographics",
            {
                "fields": (
                    "nationality",
                    "nationality_other",
                    "region",
                    "district",
                    "patient_know_dob",
                    "patient_dob",
                    "age_in_years",
                    "gender",
                    "hospital_id",
                    "initials",
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

    search_fields = ("screening_identifier",)

    radio_fields = {
        "screening_consent": admin.VERTICAL,
        "clinic_type": admin.VERTICAL,
        "patient_category": admin.VERTICAL,
        "nationality": admin.VERTICAL,
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

    def response_post_save_add(self, request, obj):
        next = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(next)

    def response_post_save_change(self, request, obj):
        next = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(next)

    def demographics(self, obj=None):
        return mark_safe(f"{obj.get_gender_display()} {obj.age_in_years}yrs ")

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True

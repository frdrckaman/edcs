from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import FollowUpForm
from ..models import FollowUp
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(FollowUp, site=edcs_subject_admin)
class FollowUpAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = FollowUpForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "VITAL SIGNS",
            {
                "fields": (
                    "sys_blood_pressure",
                    "dia_blood_pressure",
                    "temperature",
                    "respiratory_rate",
                    "pulse",
                    "weight",
                ),
            },
        ),
        (
            "TEST ORDERED",
            {
                "fields": (
                    "test_ordered_nw",
                    "test_ordered_other",
                    "test_ordered_result",
                    "hiv_status",
                    "viral_load_cd4_off",
                    "current_viral_load",
                    "current_cd4_count",
                    "hiv_genotype",
                    "CT_scan_done",
                    "CT_scan_results",
                    "CT_scan_no_results",
                    "CBC_done",
                    "CBC_results",
                    "CBC_no_results",
                    "liver_renal_test_done",
                    "liver_renal_test_results",
                    "liver_renal_test_no_results",
                ),
            },
        ),
        (
            "CLINICAL PRESENTATION (Assess for before and after symptoms)",
            {
                "fields": (
                    "breathlessness_before",
                    "breathlessness_after",
                    "tiredness_before",
                    "tiredness_after",
                    "wheezing_before",
                    "wheezing_after",
                    "shortness_breath_before",
                    "shortness_breath_after",
                    "anorexia_before",
                    "anorexia_after",
                    "cough_before",
                    "cough_after",
                    "cough_get_worse_before",
                    "cough_get_worse_after",
                    "coughing_blood_before",
                    "coughing_blood_after",
                    "chest_infections_before",
                    "chest_infections_after",
                    "chest_pain_before",
                    "chest_pain_after",
                    "hospitalized_before",
                    "hospitalized_after",
                ),
            },
        ),
        (
            "QUALITY OF LIFE (Assess if there is improvement in quality of life)",
            {
                "fields": (
                    "walk_before",
                    "walk_after",
                    "daily_activities_before",
                    "daily_activities_after",
                    "pain_assess_before",
                    "pain_assess_after",
                ),
            },
        ),
        (
            "PATIENT STATUS",
            {
                "fields": (
                    "patient_visit_status",
                    "respond_treatment",
                    "treatment_change",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "weight",
        "hiv_status",
        "current_viral_load",
        "current_cd4_count",
        "patient_visit_status",
    )

    list_filter = (
        "report_datetime",
        "weight",
        "patient_visit_status",
        "hiv_status",
        "hiv_genotype",
    )

    search_fields = ("report_datetime", "subject_visit")

    filter_horizontal = [
        "test_ordered_nw",
    ]

    radio_fields = {
        "hiv_status": admin.VERTICAL,
        "hiv_genotype": admin.VERTICAL,
        "CT_scan_done": admin.VERTICAL,
        "CT_scan_results": admin.VERTICAL,
        "CBC_done": admin.VERTICAL,
        "CBC_results": admin.VERTICAL,
        "liver_renal_test_done": admin.VERTICAL,
        "liver_renal_test_results": admin.VERTICAL,
        "breathlessness_before": admin.VERTICAL,
        "breathlessness_after": admin.VERTICAL,
        "tiredness_before": admin.VERTICAL,
        "tiredness_after": admin.VERTICAL,
        "wheezing_before": admin.VERTICAL,
        "wheezing_after": admin.VERTICAL,
        "shortness_breath_before": admin.VERTICAL,
        "shortness_breath_after": admin.VERTICAL,
        "anorexia_before": admin.VERTICAL,
        "anorexia_after": admin.VERTICAL,
        "cough_before": admin.VERTICAL,
        "cough_after": admin.VERTICAL,
        "cough_get_worse_before": admin.VERTICAL,
        "cough_get_worse_after": admin.VERTICAL,
        "coughing_blood_before": admin.VERTICAL,
        "coughing_blood_after": admin.VERTICAL,
        "chest_infections_before": admin.VERTICAL,
        "chest_infections_after": admin.VERTICAL,
        "chest_pain_before": admin.VERTICAL,
        "chest_pain_after": admin.VERTICAL,
        "hospitalized_before": admin.VERTICAL,
        "hospitalized_after": admin.VERTICAL,
        "walk_before": admin.VERTICAL,
        "walk_after": admin.VERTICAL,
        "daily_activities_before": admin.VERTICAL,
        "daily_activities_after": admin.VERTICAL,
        "pain_assess_before": admin.VERTICAL,
        "pain_assess_after": admin.VERTICAL,
        "patient_visit_status": admin.VERTICAL,
        "respond_treatment": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

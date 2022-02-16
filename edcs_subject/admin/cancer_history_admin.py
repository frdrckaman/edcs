from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin
from .modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import edcs_subject_admin
from ..forms.cancer_history_form import CancerHistoryForm
from ..models import CancerHistory


@admin.register(CancerHistory, site=edcs_subject_admin)
class CancerHistoryAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = CancerHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "CANCER DIAGNOSIS",
            {
                "fields": (
                    "cancer_dx",
                ),
            },
        ),
        (
            "BREAST CANCER",
            {
                "fields": (
                    "breast_cancer",
                    "breast_cancer_age_dx",
                    "breast_cancer_family_member",
                    "breast_cancer_family_member_other",
                ),
            },
        ),
        (
            "COLON CANCER",
            {
                "fields": (
                    "colon_cancer",
                    "colon_cancer_age_dx",
                    "colon_cancer_family_member",
                    "colon_cancer_family_member_other",
                ),
            },
        ),
        (
            "LUNG CANCER",
            {
                "fields": (
                    "lung_cancer",
                    "lung_cancer_age_dx",
                    "lung_cancer_family_member",
                    "lung_cancer_family_member_other",
                ),
            },
        ),
        (
            "OVARIAN CANCER",
            {
                "fields": (
                    "ovarian_cancer",
                    "ovarian_cancer_age_dx",
                    "ovarian_cancer_family_member",
                    "ovarian_cancer_family_member_other",
                ),
            },
        ),
        (
            "PROSTATE CANCER",
            {
                "fields": (
                    "prostate_cancer",
                    "prostate_cancer_age_dx",
                    "prostate_cancer_family_member",
                    "prostate_cancer_family_member_other",
                ),
            },
        ),
        (
            "THYROID CANCER",
            {
                "fields": (
                    "thyroid_cancer",
                    "thyroid_cancer_age_dx",
                    "thyroid_cancer_family_member",
                    "thyroid_cancer_family_member_other",
                ),
            },
        ),
        (
            "UTERINE CANCER",
            {
                "fields": (
                    "uterine_cancer",
                    "uterine_cancer_age_dx",
                    "uterine_cancer_family_member",
                    "uterine_cancer_family_member_other",
                ),
            },
        ),

        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "cancer_dx",
        "created",
    )

    list_filter = (
        "report_datetime",
        "cancer_dx",
        "breast_cancer",
        "colon_cancer",
        "lung_cancer",
        "ovarian_cancer",
        "prostate_cancer",
        "thyroid_cancer",
        "uterine_cancer",
    )

    filter_horizontal = [
        "breast_cancer_family_member",
        "colon_cancer_family_member",
        "lung_cancer_family_member",
        "ovarian_cancer_family_member",
        "prostate_cancer_family_member",
        "thyroid_cancer_family_member",
        "uterine_cancer_family_member",
    ]

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "cancer_dx": admin.VERTICAL,
        "breast_cancer": admin.VERTICAL,
        "colon_cancer": admin.VERTICAL,
        "lung_cancer": admin.VERTICAL,
        "ovarian_cancer": admin.VERTICAL,
        "prostate_cancer": admin.VERTICAL,
        "thyroid_cancer": admin.VERTICAL,
        "uterine_cancer": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

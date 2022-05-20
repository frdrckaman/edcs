from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import ClinicalReviewForm
from ..models import ClinicalReview
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ClinicalReview, site=edcs_subject_admin)
class SubjectClinicalReviewAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = ClinicalReviewForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "HIV",
            {
                "fields": (
                    "hiv_test",
                    "hiv_test_date",
                    "hiv_dx",
                    "arv",
                    "arv_start_date",
                    "arv_regularly",
                    "miss_taking_arv",
                    "miss_taking_arv_other",
                ),
            },
        ),
        (
            "LUNG DISEASES",
            {
                "fields": (
                    "lung_diseases_dx",
                    "copd_dx_date",
                    "asthma_dx_date",
                    "interstitial_lung_disease_dx_date",
                    "use_lung_diseases_medication",
                    "lung_diseases_medication",
                ),
            },
        ),
        (
            "HYPERTENSION",
            {
                "fields": (
                    "htn_dx",
                    "htn_dx_date",
                    "use_htn_medication",
                    "htn_medication",
                ),
            },
        ),
        (
            "DIABETES",
            {
                "fields": (
                    "dm_dx",
                    "dm_dx_date",
                    "use_dm_medication",
                    "dm_medication",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hiv_dx",
        "lung_diseases_dx",
        "htn_dx",
        "dm_dx",
        "created",
    )

    list_filter = (
        "report_datetime",
        "hiv_dx",
        "lung_diseases_dx",
        "htn_dx",
        "dm_dx",
    )

    search_fields = ("report_datetime",)

    radio_fields = {
        "hiv_test": admin.VERTICAL,
        "hiv_dx": admin.VERTICAL,
        "arv": admin.VERTICAL,
        "arv_regularly": admin.VERTICAL,
        "miss_taking_arv": admin.VERTICAL,
        "lung_diseases_dx": admin.VERTICAL,
        "use_lung_diseases_medication": admin.VERTICAL,
        "htn_dx": admin.VERTICAL,
        "use_htn_medication": admin.VERTICAL,
        "dm_dx": admin.VERTICAL,
        "use_dm_medication": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

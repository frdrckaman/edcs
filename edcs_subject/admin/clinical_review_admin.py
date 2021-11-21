from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..models import ClinicalReview


@admin.register(ClinicalReview, site=edcs_subject_admin)
class SubjectClinicalReviewAdmin(SimpleHistoryAdmin):
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
        ],
        [
            "LUNG DISEASES",
            {
                "fields": (
                    "lung_diseases_dx",
                    "lung_diseases_date",
                    "use_lung_diseases_medication",
                ),
            },
        ],
        [
            "HYPERTENSION",
            {
                "fields": (
                    "htn_dx",
                    "htn_dx_date",
                    "use_htn_medication",
                    "htn_medication",
                ),
            },
        ],
        [
            "DIABETES",
            {
                "fields": (
                    "dm_dx",
                    "dm_dx_date",
                    "use_dm_medication",
                    "dm_medication",
                ),
            },
        ],
        [
            "TUBERCULOSIS",
            {
                "fields": (
                    "tb_test",
                    "provide_sputum_tb_dx",
                    "tb_status",
                ),
            },
        ],
        [
            "MALIGNANCY AND LUNG CANCER",
            {
                "fields": (
                    "malignancy",
                    "lung_cancer_dx",
                ),
            },
        ],

        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "hiv_dx",
        "lung_diseases_dx",
        "htn_dx",
        "dm_dx",
        "tb_status",
        "malignancy",
        "lung_cancer_dx",
        "created",
    )

    list_filter = (
        "report_datetime",
        "hiv_dx",
        "lung_diseases_dx",
        "htn_dx",
        "dm_dx",
        "tb_status",
        "malignancy",
        "lung_cancer_dx",
    )

    search_fields = (
        "report_datetime",
    )

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
        "malignancy": admin.VERTICAL,
        "tb_test": admin.VERTICAL,
        "provide_sputum_tb_dx": admin.VERTICAL,
        "tb_status": admin.VERTICAL,
        "lung_cancer_dx": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

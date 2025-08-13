from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin
from edcs_subject.models.chemotherapy_drugs import ChemotherapyDrugs

from ..admin_site import edcs_subject_admin

# from ..forms import LungCancerTreatmentForm
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ChemotherapyDrugs, site=edcs_subject_admin)
class ChemotherapyDrugsAdmin(SimpleHistoryAdmin):

    # form = LungCancerTreatmentForm

    fieldsets = (
        (
            "CHEMOTHERAPY DRUG",
            {
                "fields": (
                    "lung_cancer_treatment",
                    "chemotherapy_drug",
                    "number_of_cycles",
                ),
            },
        ),
        # crf_status_fieldset_tuple,
        # audit_fieldset_tuple,
    )

    list_display = (
        # "report_datetime",
        "chemotherapy_drug",
        "number_of_cycles",
    )

    list_filter = (
        # "report_datetime",
        # "chemotherapy_drug",
    )

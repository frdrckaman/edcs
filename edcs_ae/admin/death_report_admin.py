from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin
from edcs_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import edcs_ae_admin
from ..forms import DeathReportForm
from ..models import DeathReport


@admin.register(DeathReport, site=edcs_ae_admin)
class DeathReportAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = DeathReportForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "subject_identifier",
                    "report_datetime",
                    "death_date",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "death_location",
                    "hospital_name",
                )
            },
        ),
        (
            "Informant Information",
            {
                "fields": (
                    "informant_contact",
                    "informant_relationship",
                    "other_informant_relationship",
                )
            },
        ),
        (
            "Cause of death",
            {
                "description": (
                    "If death occurred in hospital or a death certificate is available, "
                    "please indicate the recorded causes of death"
                ),
                "fields": (
                    "cause_of_death",
                    "cause_of_death_other",
                    "secondary_cause_of_death",
                    "secondary_cause_of_death_other",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    radio_fields = {
        "death_location": admin.VERTICAL,
        "informant_relationship": admin.VERTICAL,
    }

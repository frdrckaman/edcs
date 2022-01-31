from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import CovidInfectionHistory


@admin.register(CovidInfectionHistory, site=edcs_subject_admin)
class CovidInfectionHistoryAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):
    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "COVID-19 INFECTION HISTORY",
            {
                "fields": (
                    "think_had_covid",
                    "date_think_had_covid",
                    "have_covid_symptoms",
                    "covid_symptoms",
                    "admitted_hospital",
                    "swab_test",
                    "swab_test_results",
                    "date_first_positive_test",
                    "date_last_negative_test",
                    "covid_vaccine",
                    "vaccine_provider",
                    "no_covid_vaccine",
                    "date_recent_vaccination",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "think_had_covid",
        "swab_test",
        "swab_test_results",
        "no_covid_vaccine",
    )

    list_filter = (
        "report_datetime",
        "think_had_covid",
        "swab_test",
        "swab_test_results",
        "no_covid_vaccine",
    )

    search_fields = (
        "report_datetime",
    )

    radio_fields = {
        "think_had_covid": admin.VERTICAL,
        "have_covid_symptoms": admin.VERTICAL,
        "covid_symptoms": admin.VERTICAL,
        "admitted_hospital": admin.VERTICAL,
        "swab_test": admin.VERTICAL,
        "swab_test_results": admin.VERTICAL,
        "covid_vaccinated": admin.VERTICAL,
        "covid_vaccine": admin.VERTICAL,
        "vaccine_provider": admin.VERTICAL,
        "no_covid_vaccine": admin.VERTICAL,
    }

    def post_url_on_delete_kwargs(self, request, obj):
        return {}

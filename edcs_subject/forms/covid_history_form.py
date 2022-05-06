from django import forms

from edcs_constants.constants import NEGATIVE_TEST, OTHER, POSITIVE_TEST, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import CovidInfectionHistory


class CovidInfectionHistoryFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            YES, field="think_had_covid", field_required="date_think_had_covid"
        )
        self.applicable_if(
            YES, field="think_had_covid", field_applicable="have_covid_symptoms"
        )
        self.m2m_required_if(
            YES, field="have_covid_symptoms", m2m_field="covid_symptoms"
        )
        self.applicable_if(
            YES, field="think_had_covid", field_applicable="admitted_hospital"
        )
        self.applicable_if(YES, field="swab_test", field_applicable="swab_test_results")
        self.required_if(
            POSITIVE_TEST,
            field="swab_test_results",
            field_required="date_first_positive_test",
        )
        self.required_if(
            NEGATIVE_TEST,
            field="swab_test_results",
            field_required="date_last_negative_test",
        )
        # self.applicable_if(
        #     YES, field="covid_vaccinated", field_applicable="covid_vaccine"
        # )
        self.m2m_required_if(YES, field="covid_vaccinated", m2m_field="covid_vaccine")
        self.required_if(
            OTHER, field="covid_vaccine", field_required="covid_vaccine_other"
        )
        self.applicable_if(
            YES, field="covid_vaccinated", field_applicable="vaccine_provider"
        )
        self.required_if(
            OTHER, field="vaccine_provider", field_required="vaccine_provider_other"
        )
        self.applicable_if(
            YES, field="covid_vaccinated", field_applicable="no_covid_vaccine"
        )
        self.required_if(
            YES, field="covid_vaccinated", field_required="date_recent_vaccination"
        )


class CovidInfectionHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = CovidInfectionHistoryFormValidator

    class Meta:
        model = CovidInfectionHistory
        fields = "__all__"

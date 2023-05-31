from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import PreAirQuality


class PreAirQualityFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER,
            field="cooking_fuel",
            field_required="cooking_fuel_other",
        )
        self.applicable_if(
            YES,
            field="previously_used_cooking_fuel",
            field_applicable="previously_cooking_fuel",
        )
        self.required_if(
            OTHER,
            field="previously_cooking_fuel",
            field_required="previously_cooking_fuel_other",
        )


class PreAirQualityForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = PreAirQualityFormValidator

    class Meta:
        model = PreAirQuality
        fields = "__all__"

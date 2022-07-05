from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import PostAirQuality


class PostAirQualityFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER,
            field="cooking_fuel_used",
            field_required="cooking_fuel_used_other",
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="other_cooking_fuel",
            field_other="other_cooking_fuel_other",
        )
        self.required_if(
            OTHER,
            field="primary_fuel_heating",
            field_required="primary_fuel_heating_other",
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="solid_fuel",
            field_other="solid_fuel_other",
        )


class PostAirQualityForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = PostAirQualityFormValidator

    class Meta:
        model = PostAirQuality
        fields = "__all__"

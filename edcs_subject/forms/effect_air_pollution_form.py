from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import EffectAirPollution


class EffectAirPollutionFormValidator(FormValidator):
    def clean(self):

        self.applicable_if(
            YES, field="family_member_sickness", field_applicable="who_had_illness"
        )
        self.required_if(
            YES, field="family_member_sickness", field_required="fuel_before_changing"
        )
        self.required_if(
            YES,
            field="variation_btn_fuel",
            field_required="influence_variation_btn_fuel",
        )


class EffectAirPollutionForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = EffectAirPollutionFormValidator

    class Meta:
        model = EffectAirPollution
        fields = "__all__"

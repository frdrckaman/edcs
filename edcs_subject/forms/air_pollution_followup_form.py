from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import AirPollutionFollowUp


class AirPollutionFollowupFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER, field="fuel_type_used", field_required="fuel_type_used_other"
        )
        self.required_if(
            OTHER, field="stove_type_used", field_required="stove_type_used_other"
        )


class AirPollutionFollowupForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = AirPollutionFollowupFormValidator

    class Meta:
        model = AirPollutionFollowUp
        fields = "__all__"

from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import DemographicCharacteristic


class DemographicCharacteristicFormValidator(FormValidator):
    def clean(self):
        self.required_if(OTHER, field="education", field_required="education_other")
        self.required_if(OTHER, field="occupation", field_required="occupation_other")


class DemographicCharacteristicForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DemographicCharacteristicFormValidator

    class Meta:
        model = DemographicCharacteristic
        fields = "__all__"

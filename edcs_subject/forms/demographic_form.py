from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import DemographicCharacteristic


class DemographicCharacteristicFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.occupation = self.cleaned_data.get("occupation")
        self.occupation_details = self.cleaned_data.get("occupation_details")

    def clean(self):
        self.required_if(OTHER, field="education", field_required="education_other")
        self.required_if(OTHER, field="occupation", field_required="occupation_other")
        self.validate_occupation()

    def validate_occupation(self):
        if (
            self.occupation
            in [
                "civil_servant",
                "peasant",
                "petty_trader",
                "entrepreneur",
                "business_man",
                "casual_laborers",
            ]
        ) and self.occupation_details is None:

            raise forms.ValidationError({"occupation_details": "This field is required"})


class DemographicCharacteristicForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DemographicCharacteristicFormValidator

    class Meta:
        model = DemographicCharacteristic
        fields = "__all__"

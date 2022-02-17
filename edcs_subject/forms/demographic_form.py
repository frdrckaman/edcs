from django import forms
from edcs_constants.constants import YES, OTHER, POSITIVE_TEST, NEGATIVE_TEST

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import DemographicCharacteristic


class DemographicCharacteristicFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean(self):
        super().clean()

        self.required_if(OTHER, field="education", field_required="education_other")
        self.required_if(OTHER, field="occupation", field_required="occupation_other")
        self.required_if(OTHER, field="material_build_floor", field_required="material_build_floor_other")
        self.required_if(OTHER, field="material_build_walls", field_required="material_build_walls_other")
        self.required_if(OTHER, field="material_build_roof", field_required="material_build_roof_other")
        self.required_if(OTHER, field="use_in_cooking", field_required="use_in_cooking_other")
        self.required_if(OTHER, field="main_power_source", field_required="main_power_source_other")


class DemographicCharacteristicForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = DemographicCharacteristicFormValidator

    class Meta:
        model = DemographicCharacteristic
        fields = "__all__"

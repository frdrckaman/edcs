from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import SocioEconomicCharacteristic


class SocioEconomicCharacteristicFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER,
            field="material_build_floor",
            field_required="material_build_floor_other",
        )
        self.required_if(
            OTHER,
            field="material_build_walls",
            field_required="material_build_walls_other",
        )
        self.required_if(
            OTHER,
            field="material_build_roof",
            field_required="material_build_roof_other",
        )
        self.required_if(
            OTHER, field="use_in_cooking", field_required="use_in_cooking_other"
        )
        self.required_if(
            OTHER, field="main_power_source", field_required="main_power_source_other"
        )


class SocioEconomicCharacteristicForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = SocioEconomicCharacteristicFormValidator

    class Meta:
        model = SocioEconomicCharacteristic
        fields = "__all__"

from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LabPartD


class LabPartDFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER,
            field="hiv_drug_resistance_test",
            field_required="hiv_drug_resistance_other",
        )


class LabPartDForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartDFormValidator

    class Meta:
        model = LabPartD
        fields = "__all__"

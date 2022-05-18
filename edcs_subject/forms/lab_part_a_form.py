from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LabPartA


class LabPartAFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER, field="type_tb_test", field_required="type_tb_test_other"
        )


class LabPartAForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartAFormValidator

    class Meta:
        model = LabPartA
        fields = "__all__"

from django import forms

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator
from ..constants import NON_SMALL_CELL

from ..models import LabPartC


class LabPartCFormValidator(FormValidator):
    def clean(self):
        self.applicable_if(
            NON_SMALL_CELL, field="type_lung_ca", field_applicable="non_small_cell"
        )


class LabPartCForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartCFormValidator

    class Meta:
        model = LabPartC
        fields = "__all__"

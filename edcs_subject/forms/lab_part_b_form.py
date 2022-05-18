from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LabPartB


class LabPartBFormValidator(FormValidator):
    pass


class LabPartBForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartBFormValidator

    class Meta:
        model = LabPartB
        fields = "__all__"

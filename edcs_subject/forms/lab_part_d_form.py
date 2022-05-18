from django import forms

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LabPartD


class LabPartDFormValidator(FormValidator):
    pass


class LabPartDForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartDFormValidator

    class Meta:
        model = LabPartD
        fields = "__all__"

from django import forms
from edcs_constants.constants import OTHER, YES

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import SignSymptomLungCancer


class SignSymptomLungCancerFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean(self):
        super().clean()


class SignSymptomLungCancerForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = SignSymptomLungCancerFormValidator

    class Meta:
        model = SignSymptomLungCancer
        fields = "__all__"

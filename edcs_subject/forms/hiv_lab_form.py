from django import forms
from edcs_constants.constants import OTHER, YES

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import HivLabInvestigation


class HivLabInvestigationFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean(self):
        super().clean()


class HivLabInvestigationForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = HivLabInvestigationFormValidator

    class Meta:
        model = HivLabInvestigation
        fields = "__all__"

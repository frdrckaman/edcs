from django import forms
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import HomeLocator


class HomeLocatorFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean(self):
        super().clean()


class HomeLocatorForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = HomeLocatorFormValidator

    class Meta:
        model = HomeLocator
        fields = "__all__"

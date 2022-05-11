from django import forms

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import HomeLocator


class HomeLocatorFormValidator(FormValidator):
    pass


class HomeLocatorForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = HomeLocatorFormValidator

    class Meta:
        model = HomeLocator
        fields = "__all__"

from django import forms
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import HouseKitchenSurrounding


class HouseKitchenSurroundingFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def clean(self):
        super().clean()


class HouseKitchenSurroundingForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = HouseKitchenSurroundingFormValidator

    class Meta:
        model = HouseKitchenSurrounding
        fields = "__all__"

from django import forms

from edcs_form_validators import FormValidator, FormValidatorMixin

from ..constants import HOSPITAL_CLINIC
from ..models import DeathReport


class DeathReportFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            HOSPITAL_CLINIC,
            field="death_location",
            field_required="hospital_name",
        )

        self.validate_other_specify(
            field="informant_relationship",
            other_specify_field="other_informant_relationship",
        )


class DeathReportForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = "__all__"

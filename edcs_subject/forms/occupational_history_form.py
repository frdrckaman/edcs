from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import OccupationalHistory


class OccupationalHistoryFormValidator(FormValidator):
    def clean(self):
        super().clean()

        self.applicable_if(
            YES,
            field="history_working_industries",
            field_applicable="industries_worked",
        )
        self.required_if(
            OTHER, field="industries_worked", field_required="industries_worked_other"
        )
        self.applicable_if(
            YES, field="history_working_mines", field_applicable="how_long_work_mine"
        )


class OccupationalHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = OccupationalHistoryFormValidator

    class Meta:
        model = OccupationalHistory
        fields = "__all__"

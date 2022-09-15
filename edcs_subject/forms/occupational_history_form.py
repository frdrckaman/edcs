from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import OccupationalHistory


class OccupationalHistoryFormValidator(FormValidator):
    def clean(self):

        self.applicable_if(
            YES,
            field="history_working_industries",
            field_applicable="industries_worked",
        )
        self.m2m_other_specify(
            OTHER, m2m_field="industries_worked", field_other="industries_worked_other"
        )
        self.applicable_if(
            YES, field="history_working_mines", field_applicable="how_long_work_mine"
        )


class OccupationalHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = OccupationalHistoryFormValidator

    class Meta:
        model = OccupationalHistory
        fields = "__all__"

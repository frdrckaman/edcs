from django import forms

from edcs_constants.constants import NOT_APPLICABLE, OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import OccupationalHistory


class OccupationalHistoryFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.history_working_industries = self.cleaned_data.get("history_working_industries")
        self.industries_worked = (
            self.cleaned_data.get("industries_worked").filter(name=NOT_APPLICABLE).exists()
        )
        self.industries_working = self.cleaned_data.get("industries_worked")

    def clean(self):
        self.m2m_other_specify(
            OTHER, m2m_field="industries_worked", field_other="industries_worked_other"
        )
        self.applicable_if(
            YES, field="history_working_mines", field_applicable="how_long_work_mine"
        )
        self.validate_industries_worked()
        self.validate_industries_worked_na()
        self.validate_industries_working_na()

    def validate_industries_worked(self):
        if self.history_working_industries == YES and self.industries_worked:
            raise forms.ValidationError(
                {"industries_worked": "Not applicable is not a valid choice "}
            )

    def validate_industries_worked_na(self):
        if (self.industries_working.count() > 1) and self.history_working_industries != YES:
            raise forms.ValidationError(
                {"industries_worked": "Not applicable is the only Valid choice "}
            )

    def validate_industries_working_na(self):
        if (
            (self.industries_working.count() == 1)
            and self.history_working_industries != YES
            and not self.industries_worked
        ):
            raise forms.ValidationError(
                {"industries_worked": "Not applicable is the only Valid choice "}
            )


class OccupationalHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = OccupationalHistoryFormValidator

    class Meta:
        model = OccupationalHistory
        fields = "__all__"

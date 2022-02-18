from django import forms
from edcs_constants.constants import OTHER, NOT_APPLICABLE

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LungCancerTreatment


class LungCancerTreatmentFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.lung_cancer_stage = self.cleaned_data.get("lung_cancer_stage")
        self.date_start_treatment = self.cleaned_data.get("date_start_treatment")
        self.treatment = self.cleaned_data.get("treatment")

    def clean(self):
        super().clean()

        self.validate_date_start_treatment()

        self.validate_treatment()

        self.required_if(OTHER, field="treatment", field_required="treatment_other")

    def validate_date_start_treatment(self):
        if self.lung_cancer_stage == NOT_APPLICABLE and self.date_start_treatment is not None:
            raise forms.ValidationError(
                {
                    "date_start_treatment": "This field is not Applicable "
                }
            )
        elif self.lung_cancer_stage != NOT_APPLICABLE and self.date_start_treatment is None:
            raise forms.ValidationError(
                {
                    "date_start_treatment": "This field is Required "
                }
            )

    def validate_treatment(self):
        if self.lung_cancer_stage == NOT_APPLICABLE and self.treatment is not None:
            raise forms.ValidationError(
                {
                    "treatment": "This field is not Applicable "
                }
            )


class LungCancerTreatmentForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = LungCancerTreatmentFormValidator

    class Meta:
        model = LungCancerTreatment
        fields = "__all__"

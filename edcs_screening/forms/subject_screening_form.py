from datetime import date

from django import forms

from edcs_constants.constants import NO, OTHER, YES
from edcs_form_validators import FormValidator, FormValidatorMixin
from edcs_screening.modelform_mixins import AlreadyConsentedFormMixin
from edcs_utils import age

from ..models import SubjectScreening


class SubjectScreeningFormValidator(FormValidator):
    def clean(self):
        if (
            not self.cleaned_data.get("screening_consent")
            or self.cleaned_data.get("screening_consent") != YES
        ):
            raise forms.ValidationError(
                {
                    "screening_consent": (
                        "You may NOT screen this subject without their verbal consent."
                    )
                }
            )
        self.required_if(YES, field="patient_know_dob", field_required="patient_dob")
        self.required_if(OTHER, field="nationality", field_required="nationality_other")

        if self.cleaned_data.get("patient_dob") is not None:
            age_in_years = age(self.cleaned_data.get("patient_dob"), date.today()).years
            if age_in_years != self.cleaned_data.get("age_in_years"):
                raise forms.ValidationError(
                    {
                        "patient_dob": "Please, Crosscheck  date of birth."
                        f"Expected age is {self.cleaned_data.get('age_in_years')}, Got {age_in_years}"
                    }
                )

        if (
            self.cleaned_data.get("age_in_years")
            and self.cleaned_data.get("age_in_years") < 18
        ):
            raise forms.ValidationError(
                {"age_in_years": "Participant must be at least 18 years old."}
            )

        if self.cleaned_data.get("above_eighteen") == NO:
            raise forms.ValidationError(
                {
                    "above_eighteen": "This must be YES, participant must be 18 years old or above."
                }
            )


class SubjectScreeningForm(
    AlreadyConsentedFormMixin, FormValidatorMixin, forms.ModelForm
):
    form_validator_cls = SubjectScreeningFormValidator

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = SubjectScreening
        fields = [
            "report_datetime",
            "screening_consent",
            "region",
            "district",
            "patient_know_dob",
            "patient_dob",
            "age_in_years",
            "gender",
            "hospital_id",
            "initials",
            "tb_diagnosis",
            "above_eighteen",
            "lung_cancer_suspect",
            "cough",
            "long_standing_cough",
            "cough_blood",
            "chest_infections",
            "chest_pain",
            "persistent_breathlessness",
            "persistent_tiredness",
            "wheezing",
            "shortness_of_breath",
            "weight_loss",
            "abnormal_chest_xrays",
            "non_resolving_infection",
            "malignancy",
            "diagnosed_lung_cancer",
        ]

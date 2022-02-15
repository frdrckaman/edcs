from pprint import pprint

from django import forms
from edcs_constants.constants import NO, YES, POS, OTHER

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import ClinicalReview


class ClinicalReviewFormValidator(FormValidator):
    def clean(self):
        super().clean()
        # hiv
        arv = self.cleaned_data.get("arv")
        hiv_dx = self.cleaned_data.get("hiv_dx")
        arv_regularly = self.cleaned_data.get("arv_regularly")
        miss_taking_arv = self.cleaned_data.get("miss_taking_arv")

        self.required_if(YES, field="hiv_test", field_required="hiv_test_date")
        self.applicable_if(YES, field="hiv_test", field_applicable="hiv_dx")
        self.applicable_if(POS, field="hiv_dx", field_applicable="arv")
        self.required_if(YES, field="arv", field_required="arv_start_date")
        self.applicable_if(YES, field="arv", field_applicable="arv_regularly")
        self.applicable_if(NO, field="arv_regularly", field_applicable="miss_taking_arv")
        self.applicable_if(OTHER, field="miss_taking_arv", field_applicable="miss_taking_arv_other")

        # # htn
        self.required_if(YES, field="htn_test", field_required="htn_test_date")
        self.required_if(YES, field="htn_test", field_required="htn_reason")
        self.applicable_if(YES, field="htn_test", field_applicable="htn_dx")
        #
        # # diabetes
        # self.applicable_if_not_diagnosed(
        #     diagnoses=diagnoses,
        #     field_dx="dm_dx",
        #     field_applicable="dm_test",
        #     label="diabetes",
        # )
        # self.required_if(YES, field="dm_test", field_required="dm_test_date")
        # self.required_if(YES, field="dm_test", field_required="dm_reason")
        # self.applicable_if(YES, field="dm_test", field_applicable="dm_dx")
        #
        # self.required_if(
        #     YES,
        #     field="health_insurance",
        #     field_required="health_insurance_monthly_pay",
        #     field_required_evaluate_as_int=True,
        # )
        # self.required_if(
        #     YES,
        #     field="patient_club",
        #     field_required="patient_club_monthly_pay",
        #     field_required_evaluate_as_int=True,
        # )

    # def raise_if_dx_and_applicable(self, clinic, cond):
    #     if self.subject_screening.clinic_type in [clinic] and self.cleaned_data.get(
    #         f"{cond}_test"
    #     ) in [YES, NO]:
    #         raise forms.ValidationError(
    #             {
    #                 f"{cond}_test": (
    #                     f"Not applicable. Patient was recruited from the {cond.title} clinic."
    #                 ),
    #             }
    #         )


class ClinicalReviewForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewFormValidator

    class Meta:
        model = ClinicalReview
        fields = "__all__"

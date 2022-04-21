from django import forms

from edcs_constants.constants import (
    ASTHMA,
    COPD,
    INTERSTITIAL_LUNG_DISEASE,
    NO,
    OTHER,
    POS,
    YES,
)
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import ClinicalReview


class ClinicalReviewFormValidator(FormValidator):
    def clean(self):
        super().clean()

        # hiv
        self.required_if(YES, field="hiv_test", field_required="hiv_test_date")
        self.applicable_if(YES, field="hiv_test", field_applicable="hiv_dx")
        self.applicable_if(POS, field="hiv_dx", field_applicable="arv")
        self.required_if(YES, field="arv", field_required="arv_start_date")
        self.applicable_if(YES, field="arv", field_applicable="arv_regularly")
        self.applicable_if(
            NO, field="arv_regularly", field_applicable="miss_taking_arv"
        )
        self.required_if(
            OTHER, field="miss_taking_arv", field_required="miss_taking_arv_other"
        )

        # lung diseases
        self.required_if(COPD, field="lung_diseases_dx", field_required="copd_dx_date")
        self.required_if(
            ASTHMA, field="lung_diseases_dx", field_required="asthma_dx_date"
        )
        self.required_if(
            INTERSTITIAL_LUNG_DISEASE,
            field="lung_diseases_dx",
            field_required="interstitial_lung_disease_dx_date",
        )
        self.required_if(
            YES,
            field="use_lung_diseases_medication",
            field_required="lung_diseases_medication",
        )

        # # htn
        self.required_if(YES, field="htn_dx", field_required="htn_dx_date")
        self.applicable_if(YES, field="htn_dx", field_applicable="use_htn_medication")
        self.required_if(
            YES, field="use_htn_medication", field_required="htn_medication"
        )

        # diabetes
        self.required_if(YES, field="dm_dx", field_required="dm_dx_date")
        self.applicable_if(YES, field="dm_dx", field_applicable="use_dm_medication")
        self.required_if(YES, field="use_dm_medication", field_required="dm_medication")


class ClinicalReviewForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ClinicalReviewFormValidator

    class Meta:
        model = ClinicalReview
        fields = "__all__"

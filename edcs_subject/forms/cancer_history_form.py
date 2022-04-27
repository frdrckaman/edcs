from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import CancerHistory


class CancerHistoryFormValidator(FormValidator):
    def clean(self):
        self.applicable_if(YES, field="cancer_dx", field_applicable="breast_cancer")
        self.required_if(
            YES, field="breast_cancer", field_required="breast_cancer_age_dx"
        )
        self.required_if(
            YES, field="breast_cancer", field_required="breast_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="breast_cancer_family_member",
            field_other="breast_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="colon_cancer")
        self.required_if(
            YES, field="colon_cancer", field_required="colon_cancer_age_dx"
        )
        self.required_if(
            YES, field="colon_cancer", field_required="colon_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="colon_cancer_family_member",
            field_other="colon_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="lung_cancer")
        self.required_if(YES, field="lung_cancer", field_required="lung_cancer_age_dx")
        self.required_if(
            YES, field="lung_cancer", field_required="lung_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="lung_cancer_family_member",
            field_other="lung_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="ovarian_cancer")
        self.required_if(
            YES, field="ovarian_cancer", field_required="ovarian_cancer_age_dx"
        )
        self.required_if(
            YES, field="ovarian_cancer", field_required="ovarian_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="ovarian_cancer_family_member",
            field_other="ovarian_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="prostate_cancer")
        self.required_if(
            YES, field="prostate_cancer", field_required="prostate_cancer_age_dx"
        )
        self.required_if(
            YES, field="prostate_cancer", field_required="prostate_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="prostate_cancer_family_member",
            field_other="prostate_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="thyroid_cancer")
        self.required_if(
            YES, field="thyroid_cancer", field_required="thyroid_cancer_age_dx"
        )
        self.required_if(
            YES, field="thyroid_cancer", field_required="thyroid_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="thyroid_cancer_family_member",
            field_other="thyroid_cancer_family_member_other",
        )
        self.applicable_if(YES, field="cancer_dx", field_applicable="uterine_cancer")
        self.required_if(
            YES, field="uterine_cancer", field_required="uterine_cancer_age_dx"
        )
        self.required_if(
            YES, field="uterine_cancer", field_required="uterine_cancer_family_member"
        )
        self.m2m_other_specify(
            OTHER,
            m2m_field="uterine_cancer_family_member",
            field_other="uterine_cancer_family_member_other",
        )


class CancerHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = CancerHistoryFormValidator

    class Meta:
        model = CancerHistory
        fields = "__all__"

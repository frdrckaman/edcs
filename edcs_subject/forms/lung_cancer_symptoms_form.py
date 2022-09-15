from django import forms

from edcs_constants.constants import GREATER_THAN_6MONTHS, NONE_OF_ABOVE, OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import SignSymptomLungCancer


class SignSymptomLungCancerFormValidator(FormValidator):
    def clean(self):
        self.m2m_other_specify(
            OTHER,
            m2m_field="what_brought_hospital",
            field_other="what_brought_hospital_other",
        )
        self.required_if(
            GREATER_THAN_6MONTHS,
            field="symptoms_how_long",
            field_required="symptoms_greater_than_6months",
        )
        self.required_if(
            OTHER,
            field="characterize_symptoms",
            field_required="characterize_symptoms_other",
        )
        self.applicable_if(
            YES,
            field="family_member_same_symptoms",
            field_applicable="family_member_relationship",
        )
        self.required_if(
            OTHER,
            field="family_member_relationship",
            field_required="family_member_relationship_other",
        )
        self.required_if(YES, field="chest_radiation", field_required="no_chest_radiation")
        # self.required_if(
        #     OTHER,
        #     field="investigations_ordered",
        #     field_required="investigations_ordered_other",
        # )
        self.m2m_other_specify(
            OTHER,
            m2m_field="investigations_ordered_nw",
            field_other="what_brought_hospital_nw_other",
        )
        self.required_if(
            NONE_OF_ABOVE,
            field="investigations_ordered",
            field_required="non_investigations_ordered",
        )


class SignSymptomLungCancerForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = SignSymptomLungCancerFormValidator

    class Meta:
        model = SignSymptomLungCancer
        fields = "__all__"

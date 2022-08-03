from django import forms

from edcs_constants.constants import OTHER, POSITIVE, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..constants import NOT_RESPOND_TREATMENT
from ..models import FollowUp


class FollowUpFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER, field="test_ordered", field_required="test_ordered_other"
        )
        self.required_if(
            POSITIVE, field="hiv_status", field_required="viral_load_cd4_off"
        )
        self.required_if(
            POSITIVE, field="hiv_status", field_required="current_viral_load"
        )
        self.required_if(
            POSITIVE, field="hiv_status", field_required="current_cd4_count"
        )
        self.required_if(
            NOT_RESPOND_TREATMENT,
            field="patient_visit_status",
            field_required="respond_treatment",
        )
        self.required_if(
            YES, field="respond_treatment", field_required="treatment_change"
        )


class FollowUpForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = FollowUpFormValidator

    class Meta:
        model = FollowUp
        fields = "__all__"

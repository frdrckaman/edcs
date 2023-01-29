from django import forms

from edcs_constants.constants import NO, OTHER, POSITIVE, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..constants import NOT_RESPOND_TREATMENT
from ..models import FollowUp


class FollowUpFormValidator(FormValidator):
    def clean(self):
        self.m2m_other_specify(
            OTHER, m2m_field="test_ordered_nw", field_other="test_ordered_other"
        )
        self.required_if(POSITIVE, field="hiv_status", field_required="viral_load_cd4_off")
        self.required_if(POSITIVE, field="hiv_status", field_required="current_viral_load")
        self.required_if(POSITIVE, field="hiv_status", field_required="current_cd4_count")
        self.not_applicable(NO, field="CT_scan_done", field_applicable="CT_scan_results")
        self.required_if(NO, field="CT_scan_results", field_required="CT_scan_no_results")
        self.not_applicable(NO, field="CBC_done", field_applicable="CBC_results")
        self.required_if(NO, field="CBC_results", field_required="CBC_no_results")
        self.not_applicable(
            NO, field="liver_renal_test_done", field_applicable="liver_renal_test_results"
        )
        self.required_if(
            NO, field="liver_renal_test_results", field_required="liver_renal_test_no_results"
        )
        self.required_if(
            NOT_RESPOND_TREATMENT,
            field="patient_visit_status",
            field_required="respond_treatment",
        )
        self.required_if(YES, field="respond_treatment", field_required="treatment_change")


class FollowUpForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = FollowUpFormValidator

    class Meta:
        model = FollowUp
        fields = "__all__"

from django import forms

from edcs_constants.constants import OTHER, POSITIVE
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import LabPartA


class LabPartAFormValidator(FormValidator):
    def clean(self):
        self.required_if(
            OTHER, field="type_tb_test", field_required="type_tb_test_other"
        )
        self.required_if(
            POSITIVE, field="hiv_rapid_test", field_required="baseline_cd4_counts"
        )
        self.required_if(
            POSITIVE, field="hiv_rapid_test", field_required="baseline_viral_load"
        )


class LabPartAForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = LabPartAFormValidator

    class Meta:
        model = LabPartA
        fields = "__all__"
        help_texts = {
            "baseline_cd4_counts": "in cells/mm3",
            "baseline_viral_load": "copies/mL. Enter 0, if ess than 10 copies/ml, "
            "less than 20 copies/ml and less than 50 copies/ml",
        }

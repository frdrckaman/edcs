from django import forms

from edcs_constants.constants import (
    NOT_APPLICABLE,
    OTHER,
    YES,
    YES_CURRENT_USER,
    YES_PAST_USER,
)
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import ContraceptiveUseReproductiveHistory


class ContraceptiveUseReproductiveHistoryFormValidator(FormValidator):
    def __init__(self):
        super().__init__()
        self.use_contraceptives = self.cleaned_data.get("use_contraceptives")
        self.how_long_use_oral_contraceptives = self.cleaned_data.get(
            "how_long_use_contraceptives"
        )

    def clean(self):
        self.validate_how_long_use_oral_contraceptives()

        self.applicable_if(
            YES,
            field="post_menopausal_hormone_therapy",
            field_applicable="how_long_post_menopausal_hormone_therapy",
        )
        self.required_if(
            OTHER, field="contraceptives", field_required="contraceptives_other"
        )

    def validate_how_long_use_oral_contraceptives(self):
        if (
            self.use_contraceptives == YES_CURRENT_USER
            or self.use_contraceptives == YES_PAST_USER
        ) and self.how_long_use_oral_contraceptives == NOT_APPLICABLE:
            raise forms.ValidationError(
                {"how_long_use_contraceptives": "This field is Applicable "}
            )


class ContraceptiveUseReproductiveHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = ContraceptiveUseReproductiveHistoryFormValidator

    class Meta:
        model = ContraceptiveUseReproductiveHistory
        fields = "__all__"

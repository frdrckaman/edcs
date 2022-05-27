from django import forms

from edcs_constants.constants import (
    DECLINE_TO_ANSWER,
    NO,
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_contraceptives = self.cleaned_data.get("use_contraceptives")
        self.how_long_use_oral_contraceptives = self.cleaned_data.get(
            "how_long_use_contraceptives"
        )

        self.contraceptives = self.cleaned_data.get("contraceptives")

        self.contraceptives_na = self.contraceptives.filter(
            name=NOT_APPLICABLE
        ).exists()

    def clean(self):
        self.validate_how_long_use_oral_contraceptives()

        self.validate_contraceptives()

        self.applicable_if(
            YES,
            field="post_menopausal_hormone_therapy",
            field_applicable="how_long_post_menopausal_hormone_therapy",
        )
        self.required_if(
            OTHER, field="contraceptives", field_required="contraceptives_other"
        )

    def validate_contraceptives(self):
        if (
            self.use_contraceptives == YES_CURRENT_USER
            or self.use_contraceptives == YES_PAST_USER
        ) and self.contraceptives_na:
            raise forms.ValidationError({"contraceptives": "This field is Applicable "})

    def validate_how_long_use_oral_contraceptives(self):
        if (
            self.use_contraceptives == YES_CURRENT_USER
            or self.use_contraceptives == YES_PAST_USER
        ) and self.how_long_use_oral_contraceptives == NOT_APPLICABLE:
            raise forms.ValidationError(
                {"how_long_use_contraceptives": "This field is Applicable "}
            )
        elif (
            self.use_contraceptives == NO
            or self.use_contraceptives == DECLINE_TO_ANSWER
            or self.use_contraceptives == NOT_APPLICABLE
        ) and (self.contraceptives.count() > 1):
            raise forms.ValidationError({"contraceptives": "Invalid choices "})
        elif (
            self.use_contraceptives == NO
            or self.use_contraceptives == DECLINE_TO_ANSWER
            or self.use_contraceptives == NOT_APPLICABLE
        ) and not self.contraceptives_na:
            raise forms.ValidationError(
                {"contraceptives": "This field is Not Applicable  "}
            )


class ContraceptiveUseReproductiveHistoryForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = ContraceptiveUseReproductiveHistoryFormValidator

    class Meta:
        model = ContraceptiveUseReproductiveHistory
        fields = "__all__"

from django import forms
from edcs_constants.constants import OTHER, NEVER, YES_CURRENT_SMOKER, YES_PAST_SMOKER, YES

from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import AirPollutionFollowUp


class AlcoholTobaccoUseFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.smoke_tobacco = self.cleaned_data.get("smoke_tobacco")
        self.tobacco_product = self.cleaned_data.get("tobacco_product")
        self.date_start_smoking = self.cleaned_data.get("date_start_smoking")
        self.smoking_frequency = self.cleaned_data.get("smoking_frequency")
        self.smoking_frequency_other = self.cleaned_data.get("smoking_frequency_other")
        self.no_tobacco_product_smoked = self.cleaned_data.get("no_tobacco_product_smoked")
        self.smoke_inside_house = self.cleaned_data.get("smoke_inside_house")
        self.smoke_inside_house_other = self.cleaned_data.get("smoke_inside_house_other")
        self.alcohol_consumption_frequency = self.cleaned_data.get("alcohol_consumption_frequency")
        self.alcohol_consumption_frequency_other = self.cleaned_data.get("alcohol_consumption_frequency_other")

    def clean(self):
        super().clean()

        self.validate_date_start_smoking()

        self.validate_smoking_frequency_other()

        self.validate_no_tobacco_product_smoked()

        self.not_applicable_if(NEVER, field="smoke_tobacco", field_applicable="tobacco_product")
        self.not_applicable_if(NEVER, field="smoke_tobacco", field_applicable="smoking_frequency")
        self.required_if(OTHER, field="smoking_frequency", field_required="smoking_frequency_other")
        self.required_if(YES_PAST_SMOKER, field="smoke_tobacco", field_required="age_start_smoking")
        self.required_if(YES_PAST_SMOKER, field="smoke_tobacco", field_required="age_stop_smoking")
        self.applicable_if(YES, field="someone_else_smoke", field_applicable="smoke_inside_house")
        self.required_if(OTHER, field="smoke_inside_house", field_required="smoke_inside_house_other")
        self.not_applicable_if(NEVER, field="consume_alcohol", field_applicable="alcohol_consumption_frequency")
        self.required_if(OTHER, field="alcohol_consumption_frequency", field_required="alcohol_consumption_frequency_other")

    def validate_date_start_smoking(self):
        if self.smoke_tobacco == NEVER and self.date_start_smoking is not None:
            raise forms.ValidationError(
                {
                    "date_start_smoking": "Date is not Applicable "
                }
            )
        elif (self.smoke_tobacco == YES_CURRENT_SMOKER or self.smoke_tobacco == YES_PAST_SMOKER) and self.date_start_smoking is None:
            raise forms.ValidationError(
                {
                    "date_start_smoking": "Date is Required "
                }
            )

    def validate_smoking_frequency_other(self):
        if self.smoking_frequency != OTHER and self.smoking_frequency_other is not None:
            raise forms.ValidationError(
                {
                    "smoking_frequency_other": "This field is not Applicable "
                }
            )

    def validate_no_tobacco_product_smoked(self):
        if (self.smoke_tobacco == YES_CURRENT_SMOKER or self.smoke_tobacco == YES_PAST_SMOKER) and self.no_tobacco_product_smoked is None:
            raise forms.ValidationError(
                {
                    "no_tobacco_product_smoked": "This field is required "
                }
            )
        elif self.smoke_tobacco == NEVER and self.no_tobacco_product_smoked is not None:
            raise forms.ValidationError(
                {
                    "no_tobacco_product_smoked": "This field is not Applicable "
                }
            )

    def validate_smoke_inside_house_other(self):
        if self.smoke_inside_house != OTHER and self.smoke_inside_house_other is not None:
            raise forms.ValidationError(
                {
                    "smoke_inside_house_other": "This field is not Applicable "
                }
            )

    def validate_alcohol_consumption_frequency_other(self):
        if self.alcohol_consumption_frequency != OTHER and self.alcohol_consumption_frequency_other is not None:
            raise forms.ValidationError(
                {
                    "alcohol_consumption_frequency_other": "This field is not Applicable "
                }
            )


class AlcoholTobaccoUseForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = AlcoholTobaccoUseFormValidator

    class Meta:
        model = AirPollutionFollowUp
        fields = "__all__"

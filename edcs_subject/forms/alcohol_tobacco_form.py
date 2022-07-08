from pprint import pprint

from django import forms
from django.db.models import Q

from edcs_constants.constants import (
    NEVER,
    NOT_APPLICABLE,
    OTHER,
    YES,
    YES_CURRENT_CHEW,
    YES_CURRENT_SMOKER,
    YES_PAST_CHEW,
    YES_PAST_SMOKER,
)
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import AirPollutionFollowUp


class AlcoholTobaccoUseFormValidator(FormValidator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.smoke_tobacco = self.cleaned_data.get("smoke_chew_tobacco")
        self.tobacco_product = self.cleaned_data.get("tobacco_products")
        self.date_start_smoking = self.cleaned_data.get("date_start_smoking")
        self.smoking_frequency = self.cleaned_data.get("smoking_frequency")
        self.smoking_frequency_other = self.cleaned_data.get("smoking_frequency_other")
        self.age_start_smoking = self.cleaned_data.get("age_start_smoking")
        self.age_stop_smoking = self.cleaned_data.get("age_stop_smoking")
        self.no_tobacco_product_smoked = self.cleaned_data.get(
            "no_tobacco_product_smoked"
        )
        self.smoke_inside_house = self.cleaned_data.get("smoke_inside_house")
        self.smoke_inside_house_other = self.cleaned_data.get(
            "smoke_inside_house_other"
        )
        self.alcohol_consumption_frequency = self.cleaned_data.get(
            "alcohol_consumption_frequency"
        )
        self.alcohol_consumption_frequency_other = self.cleaned_data.get(
            "alcohol_consumption_frequency_other"
        )
        self.never_use_tobacco = (
            self.cleaned_data.get("smoke_chew_tobacco").filter(name=NEVER).exists()
        )
        self.past_smoker = (
            self.cleaned_data.get("smoke_chew_tobacco")
            .filter(name=YES_PAST_SMOKER)
            .exists()
        )

        self.current_smoker = (
            self.cleaned_data.get("smoke_chew_tobacco")
            .filter(name=YES_CURRENT_SMOKER)
            .exists()
        )

        self.tobacco_user = (
            self.cleaned_data.get("smoke_chew_tobacco")
            .filter(
                Q(name=YES_CURRENT_SMOKER)
                | Q(name=YES_PAST_SMOKER)
                | Q(name=YES_CURRENT_CHEW)
                | Q(name=YES_PAST_CHEW)
            )
            .exists()
        )

        self.tobacco_products = self.cleaned_data.get("tobacco_products")

        self.tobacco_products_na = (
            self.cleaned_data.get("tobacco_products")
            .filter(name=NOT_APPLICABLE)
            .exists()
        )

    def clean(self):

        self.validate_smoke_chew_tobacco()

        self.validate_date_start_smoking()

        self.validate_no_tobacco_product_smoked()

        self.validate_tobacco_products()

        self.validate_tobacco_products_na()

        self.m2m_other_specify(
            OTHER, m2m_field="tobacco_products", field_other="tobacco_products_other"
        )

        self.not_applicable_if(
            NEVER, field="smoke_chew_tobacco", field_applicable="smoking_frequency"
        )
        self.required_if(
            OTHER, field="smoking_frequency", field_required="smoking_frequency_other"
        )
        self.applicable_if(
            YES, field="someone_else_smoke", field_applicable="smoke_inside_house"
        )
        self.required_if(
            OTHER, field="smoke_inside_house", field_required="smoke_inside_house_other"
        )
        self.not_applicable_if(
            NEVER,
            field="consume_alcohol",
            field_applicable="alcohol_consumption_frequency",
        )
        self.required_if(
            OTHER,
            field="alcohol_consumption_frequency",
            field_required="alcohol_consumption_frequency_other",
        )

        self.validate_age_start_smoking()

        self.validate_age_stop_smoking()

    def validate_smoke_chew_tobacco(self):
        if self.tobacco_user and self.never_use_tobacco:
            raise forms.ValidationError(
                {"smoke_chew_tobacco": "NEVER is not Applicable "}
            )

    def validate_tobacco_products(self):
        if self.tobacco_user and self.tobacco_products_na:
            raise forms.ValidationError(
                {"tobacco_products": "This field is Applicable "}
            )
        elif not self.tobacco_user and (self.tobacco_products.count() > 1):
            raise forms.ValidationError({"tobacco_products": "Invalid choices "})
        elif not self.tobacco_user and not self.tobacco_products_na:
            raise forms.ValidationError(
                {"tobacco_products": "This field is Not Applicable "}
            )

    def validate_tobacco_products_na(self):
        if (self.tobacco_products.count() > 1) and self.tobacco_products_na:
            raise forms.ValidationError(
                {"tobacco_products": "NOT APPLICABLE is not A Valid choice "}
            )

    def validate_date_start_smoking(self):
        if self.never_use_tobacco and self.date_start_smoking is not None:
            raise forms.ValidationError(
                {"date_start_smoking": "Date is not Applicable "}
            )
        elif (
            self.current_smoker or self.past_smoker
        ) and self.date_start_smoking is None:
            raise forms.ValidationError({"date_start_smoking": "Date is Required "})

    def validate_no_tobacco_product_smoked(self):
        if (
            self.current_smoker or self.past_smoker
        ) and self.no_tobacco_product_smoked is None:
            raise forms.ValidationError(
                {"no_tobacco_product_smoked": "This field is required "}
            )
        elif self.never_use_tobacco and self.no_tobacco_product_smoked is not None:
            raise forms.ValidationError(
                {"no_tobacco_product_smoked": "This field is not Applicable "}
            )

    def validate_age_start_smoking(self):
        if (self.current_smoker or self.past_smoker) and self.age_start_smoking is None:
            raise forms.ValidationError(
                {"age_start_smoking": "This field is required "}
            )

    def validate_age_stop_smoking(self):
        if self.past_smoker and self.age_stop_smoking is None:
            raise forms.ValidationError({"age_stop_smoking": "This field is required "})


class AlcoholTobaccoUseForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = AlcoholTobaccoUseFormValidator

    class Meta:
        model = AirPollutionFollowUp
        fields = "__all__"

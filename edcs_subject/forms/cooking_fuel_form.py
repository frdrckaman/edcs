from django import forms

from edcs_constants.constants import OTHER, YES
from edcs_form_validators import FormValidatorMixin
from edcs_form_validators.form_validator import FormValidator

from ..models import CookingFuel


class CookingFuelFormValidator(FormValidator):
    def clean(self):

        self.required_if(
            OTHER, field="main_use_cooking", field_required="main_use_cooking_other"
        )
        self.required_if(
            OTHER, field="cooking_done", field_required="cooking_done_other"
        )
        self.required_if(
            OTHER,
            field="neighbor_use_cooking",
            field_required="neighbor_use_cooking_other",
        )
        self.applicable_if(YES, field="use_wood", field_applicable="use_wood_per_month")
        self.applicable_if(
            YES, field="use_kerosene", field_applicable="use_kerosene_per_month"
        )
        self.applicable_if(
            YES, field="use_charcoal", field_applicable="use_charcoal_per_month"
        )
        self.applicable_if(YES, field="use_coal", field_applicable="use_coal_per_month")
        self.applicable_if(
            YES, field="use_straw", field_applicable="use_straw_per_month"
        )
        self.applicable_if(
            YES, field="use_electricity", field_applicable="use_electricity_per_month"
        )
        self.applicable_if(
            YES, field="use_biogas", field_applicable="use_biogas_per_month"
        )
        self.applicable_if(YES, field="use_dung", field_applicable="use_dung_per_month")
        self.applicable_if(
            YES, field="use_paper", field_applicable="use_paper_per_month"
        )
        self.applicable_if(
            YES, field="use_polythene", field_applicable="use_polythene_per_month"
        )


class CookingFuelForm(FormValidatorMixin, forms.ModelForm):
    form_validator_cls = CookingFuelFormValidator

    class Meta:
        model = CookingFuel
        fields = "__all__"

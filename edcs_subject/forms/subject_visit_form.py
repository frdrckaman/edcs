from django import forms

from edcs_constants.constants import OTHER
from edcs_form_validators import INVALID_ERROR, FormValidatorMixin
from edcs_sites.forms import SiteModelFormMixin

from ..constants import SCHEDULED
from ..form_validators import VisitFormValidator
from ..models import SubjectVisit


class SubjectVisitFormValidator(VisitFormValidator):
    validate_missed_visit_reason = False

    def clean(self):
        reason = self.cleaned_data.get("reason")

        if reason != SCHEDULED:
            raise forms.ValidationError(
                {"reason": "This is a schedule visit"}, code=INVALID_ERROR
            )

        self.required_if(OTHER, field="info_source", field_required="info_source_other")


class SubjectVisitForm(SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = "__all__"

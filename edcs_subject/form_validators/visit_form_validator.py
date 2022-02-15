from django import forms
from django.conf import settings
from edcs_form_validators import REQUIRED_ERROR, FormValidator

EDCS_VISIT_TRACKING_ALLOW_MISSED_UNSCHEDULED = getattr(
    settings, "EDCS_VISIT_TRACKING_ALLOW_MISSED_UNSCHEDULED", False
)


class VisitFormValidator(FormValidator):
    # visit_sequence_cls = VisitSequence
    validate_missed_visit_reason = True
    validate_unscheduled_visit_reason = True

    def clean(self) -> None:
        appointment = self.cleaned_data.get("appointment")
        if not appointment:
            raise forms.ValidationError(
                {"appointment": "This field is required"}, code=REQUIRED_ERROR
            )

    @property
    def crf_options(self) -> dict:
        appointment = self.cleaned_data.get("appointment")
        return dict(
            subject_identifier=appointment.subject_identifier,
            visit_code=appointment.visit_code,
            visit_code_sequence=appointment.visit_code_sequence,
            visit_schedule_name=appointment.visit_schedule_name,
            schedule_name=appointment.schedule_name,
            # entry_status=KEYED,
        )

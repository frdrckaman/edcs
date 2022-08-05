from arrow.arrow import Arrow
from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils.html import format_html

from edcs_form_validators.form_validator import FormValidator

# from edcs_metadata.form_validators import MetaDataFormValidatorMixin
from edcs_utils import convert_php_dateformat, get_utcnow
from edcs_visit_schedule.schedule.window import (
    ScheduledVisitWindowError,
    UnScheduledVisitWindowError,
)

from ..constants import (
    CANCELLED_APPT,
    COMPLETE_APPT,
    IN_PROGRESS_APPT,
    INCOMPLETE_APPT,
    NEW_APPT,
    UNSCHEDULED_APPT,
)


class AppointmentFormValidator(FormValidator):
    """Note, the appointment is only changed, never added,
    through this form.
    """

    appointment_model = "edcs_appointment.appointment"

    def clean(self):
        self.validate_visit_report_sequence()
        self.validate_appt_sequence()
        self.validate_not_future_appt_datetime()
        self.validate_appt_datetime_in_window()
        self.validate_appt_new_or_cancelled()
        self.validate_appt_inprogress_or_incomplete()
        self.validate_appt_inprogress()
        self.validate_appt_new_or_complete()
        self.validate_facility_name()
        self.validate_appt_reason()

    @property
    def appointment_model_cls(self):
        return django_apps.get_model(self.appointment_model)

    @property
    def required_additional_forms_exist(self):
        """Returns True if any additional required forms are
        yet to be keyed.
        """
        return False

    def validate_visit_report_sequence(self):
        """Enforce visit report sequence."""
        try:
            self.instance.visit
        except (ObjectDoesNotExist, AttributeError):
            if (
                self.cleaned_data.get("appt_status") == IN_PROGRESS_APPT
                and self.instance
            ):
                try:
                    self.instance.visit
                except ObjectDoesNotExist:
                    previous_appt = self.instance.get_previous(include_interim=True)
                    if previous_appt and previous_appt.appt_status != CANCELLED_APPT:
                        try:
                            previous_appt.visit
                        except ObjectDoesNotExist:
                            raise forms.ValidationError(
                                "A previous appointment requires a visit report. "
                                f"Update appointment {previous_appt.visit_code}."
                                f"{previous_appt.visit_code_sequence} first.",
                                code="previous_visit_missing",
                            )
        return True

    def validate_appt_sequence(self):
        """Enforce appointment and visit entry sequence.

        1. Check if previous appointment has a visit report
        2. If not check which previous appointment, if any,
        has a completed visit report
        3. If none, is this the first appointment?

        """
        if self.cleaned_data.get("appt_status") in [
            IN_PROGRESS_APPT,
            INCOMPLETE_APPT,
            COMPLETE_APPT,
        ]:
            try:
                self.instance.previous.visit
            except ObjectDoesNotExist:
                first_new_appt = (
                    self.appointment_model_cls.objects.filter(
                        subject_identifier=self.instance.subject_identifier,
                        visit_schedule_name=self.instance.visit_schedule_name,
                        schedule_name=self.instance.schedule_name,
                        appt_status=NEW_APPT,
                    )
                    .order_by("timepoint", "visit_code_sequence")
                    .first()
                )
                if first_new_appt:
                    raise forms.ValidationError(
                        "A previous appointment requires updating. "
                        f"Update appointment for {first_new_appt.visit_code} first."
                    )
            except AttributeError:
                pass
        return True

    def validate_not_future_appt_datetime(self):
        appt_datetime = self.cleaned_data.get("appt_datetime")
        if appt_datetime and appt_datetime != NEW_APPT:
            rappt_datetime = Arrow.fromdatetime(appt_datetime, appt_datetime.tzinfo)
            if rappt_datetime.to("UTC").date() > get_utcnow().date():
                raise forms.ValidationError(
                    {"appt_datetime": "Cannot be a future date."}
                )

    def validate_appt_datetime_in_window(self):
        if not self.instance.is_baseline_appt:
            baseline_timepoint_datetime = (
                self.instance.__class__.objects.first_appointment(
                    subject_identifier=self.instance.subject_identifier,
                    visit_schedule_name=self.instance.visit_schedule_name,
                    schedule_name=self.instance.schedule_name,
                ).timepoint_datetime
            )

            datestring = convert_php_dateformat(settings.SHORT_DATE_FORMAT)
            self.instance.visit_from_schedule.timepoint_datetime = (
                self.instance.timepoint_datetime
            )
            lower = self.instance.visit_from_schedule.dates.lower.strftime(datestring)
            try:
                self.instance.schedule.datetime_in_window(
                    timepoint_datetime=self.instance.timepoint_datetime,
                    dt=self.cleaned_data.get("appt_datetime"),
                    visit_code=self.instance.visit_code,
                    visit_code_sequence=self.instance.visit_code_sequence,
                    baseline_timepoint_datetime=baseline_timepoint_datetime,
                )
            except UnScheduledVisitWindowError:
                upper = self.instance.schedule.visits.next(
                    self.instance.visit_code
                ).dates.lower.strftime(datestring)
                raise forms.ValidationError(
                    {
                        "appt_datetime": (
                            f"Invalid. Expected a date between {lower} and {upper} (U)."
                        )
                    }
                )
            except ScheduledVisitWindowError:
                upper = self.instance.visit_from_schedule.dates.upper.strftime(
                    datestring
                )
                raise forms.ValidationError(
                    {
                        "appt_datetime": (
                            f"Invalid. Expected a date between {lower} and {upper} (S)."
                        )
                    }
                )

    def validate_appt_new_or_cancelled(self):
        """Don't allow new or cancelled if form data exists
        and don't allow cancelled if visit_code_sequence == 0.
        """
        appt_status = self.cleaned_data.get("appt_status")
        if (
            appt_status in [NEW_APPT, CANCELLED_APPT]
            and self.crf_metadata_required_exists
        ):
            raise forms.ValidationError(
                {"appt_status": "Invalid. CRF data has already been entered."}
            )
        elif (
            appt_status in [NEW_APPT, CANCELLED_APPT]
            and self.requisition_metadata_required_exists
        ):
            raise forms.ValidationError(
                {"appt_status": "Invalid. requisition data has already been entered."}
            )
        elif self.instance.visit_code_sequence == 0 and appt_status == CANCELLED_APPT:
            raise forms.ValidationError(
                {"appt_status": "Invalid. Appointment may not be cancelled."}
            )

    def validate_appt_inprogress_or_incomplete(self):
        appt_status = self.cleaned_data.get("appt_status")
        if (
            appt_status not in [INCOMPLETE_APPT, IN_PROGRESS_APPT]
            and self.crf_metadata_required_exists
        ):
            url = self.changelist_url("crfmetadata")
            raise forms.ValidationError(
                {
                    "appt_status": format_html(
                        f'Invalid. Not all <a href="{url}">required CRFs</a> have been keyed'
                    )
                }
            )
        elif (
            appt_status not in [INCOMPLETE_APPT, IN_PROGRESS_APPT]
            and self.requisition_metadata_required_exists
        ):
            url = self.changelist_url("requisitionmetadata")
            raise forms.ValidationError(
                {
                    "appt_status": format_html(
                        f'Invalid. Not all <a href="{url}">'
                        "required requisitions</a> have been keyed"
                    )
                }
            )

    def validate_appt_inprogress(self):
        appt_status = self.cleaned_data.get("appt_status")
        if appt_status == IN_PROGRESS_APPT and self.appointment_in_progress_exists:
            raise forms.ValidationError(
                {
                    "appt_status": (
                        "Invalid. Another appointment in this schedule is in progress."
                    )
                }
            )

    def validate_appt_new_or_complete(self):
        appt_status = self.cleaned_data.get("appt_status")
        if (
            appt_status not in [COMPLETE_APPT, NEW_APPT]
            and self.crf_metadata_exists
            and self.requisition_metadata_exists
            and not self.crf_metadata_required_exists
            and not self.requisition_metadata_required_exists
            and not self.required_additional_forms_exist
        ):
            if not self.crf_metadata_required_exists:
                raise forms.ValidationError(
                    {"appt_status": "Invalid. All required CRFs have been keyed"}
                )
            elif not self.requisition_metadata_required_exists:
                raise forms.ValidationError(
                    {
                        "appt_status": "Invalid. All required requisitions have been keyed"
                    }
                )
            elif not self.required_additional_forms_exist:
                raise forms.ValidationError(
                    {
                        "appt_status": (
                            "Invalid. All required 'additional' forms have been keyed"
                        )
                    }
                )

    @property
    def appointment_in_progress_exists(self):
        """Returns True if another appointment in this schedule
        is currently set to "in_progress".
        """
        return (
            self.appointment_model_cls.objects.filter(
                subject_identifier=self.instance.subject_identifier,
                visit_schedule_name=self.instance.visit_schedule_name,
                schedule_name=self.instance.schedule_name,
                appt_status=IN_PROGRESS_APPT,
            )
            .exclude(id=self.instance.id)
            .exists()
        )

    def validate_facility_name(self):
        """Raises if facility_name not found in edc_facility.AppConfig."""
        if self.cleaned_data.get("facility_name"):
            app_config = django_apps.get_app_config("edc_facility")
            if self.cleaned_data.get("facility_name") not in app_config.facilities:
                raise forms.ValidationError(
                    f"Facility '{self.facility_name}' does not exist."
                )

    def validate_appt_reason(self):
        """Raises if visit_code_sequence is not 0 and appt_reason
        is not UNSCHEDULED_APPT.
        """
        appt_reason = self.cleaned_data.get("appt_reason")
        appt_status = self.cleaned_data.get("appt_status")
        if (
            appt_reason
            and self.instance.visit_code_sequence
            and appt_reason != UNSCHEDULED_APPT
        ):
            raise forms.ValidationError(
                {"appt_reason": f"Expected {UNSCHEDULED_APPT.title()}"}
            )
        elif (
            appt_reason
            and not self.instance.visit_code_sequence
            and appt_reason == UNSCHEDULED_APPT
        ):
            raise forms.ValidationError(
                {"appt_reason": f"Cannot be {UNSCHEDULED_APPT.title()}"}
            )
        elif (
            appt_status
            and not self.instance.visit_code_sequence
            and appt_status == CANCELLED_APPT
        ):
            raise forms.ValidationError(
                {"appt_status": "Invalid. This is a scheduled appointment"}
            )

    def changelist_url(self, model_name):
        """Returns the model's changelist url with filter querystring"""
        url = reverse(f"edc_metadata_admin:edc_metadata_{model_name}_changelist")
        url = (
            f"{url}?q={self.instance.subject_identifier}"
            f"&visit_code={self.instance.visit_code}"
            f"&visit_code_sequence={self.instance.visit_code_sequence}"
        )
        return url

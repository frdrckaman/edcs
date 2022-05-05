from pprint import pprint

from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from pytz import timezone

from edcs_constants.constants import OTHER
from edcs_form_validators import FormValidator
from edcs_screening.utils import get_subject_screening_model_name
from edcs_utils import AgeValueError, age
from edcs_utils.date import to_utc
from edcs_utils.text import convert_php_dateformat


class SubjectConsentFormValidatorMixin(FormValidator):
    """Form Validator mixin for the consent model."""

    subject_screening_model = get_subject_screening_model_name()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._subject_screening = None
        self._consent_datetime = None
        self.dob = self.cleaned_data.get("dob")
        self.is_dob_estimated = self.cleaned_data.get("is_dob_estimated")
        self.gender = self.cleaned_data.get("gender")
        self.guardian_name = self.cleaned_data.get("guardian_name")
        self.screening_identifier = self.cleaned_data.get("screening_identifier")
        self.clinic_type = self.cleaned_data.get("clinic_type")
        self.patient_category = self.cleaned_data.get("patient_category")
        self.tz = timezone(settings.TIME_ZONE)
        self.identity = self.cleaned_data.get("identity")
        self.initials = self.cleaned_data.get("initials")
        self.nationality = self.cleaned_data.get("nationality")

    def clean(self):

        self.validate_consent_datetime()

        self.validate_clinic_type()

        self.validate_patient_category()

        self.validate_age()

        self.validate_dob_estimated()

        self.validate_screening_dob()

        self.validate_gender()

        self.validate_identity()

        self.validate_initials()

        self.validate_nationality()

        self.required_if(OTHER, field="nationality", field_required="nationality_other")

    @property
    def subject_screening_model_cls(self):
        return django_apps.get_model(self.subject_screening_model)

    @property
    def consent_datetime(self):
        if not self._consent_datetime:
            if "consent_datetime" in self.cleaned_data:
                if self.add_form and not self.cleaned_data.get("consent_datetime"):
                    raise forms.ValidationError(
                        {"consent_datetime": "This field is required."}
                    )
                self._consent_datetime = to_utc(
                    self.cleaned_data.get("consent_datetime")
                )
            else:
                self._consent_datetime = self.instance.consent_datetime
        return self._consent_datetime

    @property
    def subject_screening(self):
        if not self._subject_screening:
            try:
                self._subject_screening = self.subject_screening_model_cls.objects.get(
                    screening_identifier=self.screening_identifier
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    'Complete the "Subject Screening" form before proceeding.',
                    code="missing_subject_screening",
                )
        return self._subject_screening

    @property
    def screening_age_in_years(self) -> int:
        """Returns age in years calculated from dob relative to
        screening datetime"""
        try:
            rdelta = age(self.dob, self.subject_screening.report_datetime.date())
        except AgeValueError as e:
            raise forms.ValidationError(str(e))
        return rdelta.years

    def validate_age(self) -> None:
        """Validate age matches that on the screening form."""
        if (
            self.dob
            and self.screening_age_in_years != self.subject_screening.age_in_years
        ):
            raise forms.ValidationError(
                {
                    "dob": "Age mismatch. The date of birth entered does "
                    f"not match the age at screening. "
                    f"Expected {self.subject_screening.age_in_years}. "
                    f"Got {self.screening_age_in_years}."
                }
            )

    def validate_clinic_type(self) -> None:
        """Validate clinic_type matches that on the screening form."""
        if self.clinic_type != self.subject_screening.clinic_type:
            raise forms.ValidationError(
                {
                    "clinic_type": "Clinic Type mismatch. The Clinic Type selected does "
                    f"not match the Clinic Type selected during screening. "
                    f"Expected {self.subject_screening.clinic_type}. "
                    f"Got {self.clinic_type}."
                }
            )

    def validate_patient_category(self) -> None:
        """Validate patient_category matches that on the screening form."""
        if self.patient_category != self.subject_screening.patient_category:
            raise forms.ValidationError(
                {
                    "patient_category": "Patient Category mismatch. Patient Category selected does "
                    f"not match the Patient Category selected during screening. "
                    f"Expected {self.subject_screening.patient_category}. "
                    f"Got {self.patient_category}."
                }
            )

    def validate_dob_estimated(self) -> None:
        """Validate patient know date of birth on the screening form."""
        if (
            self.is_dob_estimated == "-"
            and self.subject_screening.patient_know_dob == "No"
        ):
            raise forms.ValidationError(
                {
                    "is_dob_estimated": "Option can not NO, "
                    f"because its specified during screening that patient does not know his/her date of birth."
                }
            )

    def validate_screening_dob(self) -> None:
        """Validate patient date of birth on the screening form."""
        if (
            self.dob != self.subject_screening.patient_dob
            and self.subject_screening.patient_know_dob == "Yes"
        ):
            raise forms.ValidationError(
                {
                    "dob": "Date mismatch. The date of birth entered does "
                    f"not match the date of birth entered at screening. "
                    f"Expected {self.subject_screening.patient_dob}. "
                    f"Got {self.dob}."
                }
            )

    def validate_gender(self) -> None:
        """Validate gender matches that on the screening form."""
        if self.gender != self.subject_screening.gender:
            raise forms.ValidationError(
                {
                    "gender": "Gender mismatch. The gender entered does "
                    f"not match that reported at screening. "
                    f"Expected '{self.subject_screening.get_gender_display()}'. "
                }
            )

    def validate_consent_datetime(self) -> None:
        """Validate consent datetime with the eligibility datetime.

        Eligibility datetime must come first.

        Watchout for timezone, cleaned_data has local TZ.
        """
        if (
            self.consent_datetime - self.subject_screening.eligibility_datetime
        ).total_seconds() < 0:
            local_dt = self.subject_screening.eligibility_datetime.astimezone(self.tz)
            formatted = local_dt.strftime(
                convert_php_dateformat(settings.SHORT_DATETIME_FORMAT)
            )
            raise forms.ValidationError(
                {
                    "consent_datetime": (
                        f"Cannot be before the date and time eligibility "
                        f"was confirmed. Eligibility was confirmed at "
                        f"{formatted}."
                    )
                },
            )

    def validate_identity(self) -> None:
        if self.identity != self.subject_screening.hospital_id:
            raise forms.ValidationError(
                {
                    "identity": "Hospital ID mismatch. The Hospital ID entered does "
                    f"not match that reported at screening. "
                    f"Expected '{self.subject_screening.hospital_id}'. "
                }
            )

    def validate_nationality(self) -> None:
        if self.nationality != self.subject_screening.nationality:
            raise forms.ValidationError(
                {
                    "nationality": "Nationality mismatch. The Nationality entered does "
                    f"not match that reported at screening. "
                    f"Expected '{self.subject_screening.nationality}'. "
                }
            )

    def validate_initials(self) -> None:
        if self.initials != self.subject_screening.initials:
            raise forms.ValidationError(
                {
                    "initials": "Patient initials mismatch. Patient initials entered does "
                    f"not match that reported at screening. "
                    f"Expected '{self.subject_screening.initials}'. "
                }
            )

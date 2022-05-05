from django.apps import apps as django_apps
from django.db import models

from edcs_consent.field_mixins import (
    CitizenFieldsMixin,
    IdentityFieldsMixin,
    PersonalFieldsMixin,
    ReviewFieldsMixin,
    SampleCollectionFieldsMixin,
    VulnerabilityFieldsMixin,
)
from edcs_consent.model_mixins import ConsentModelMixin
from edcs_constants.choices import COUNTRY, GENDER
from edcs_constants.constants import NOT_APPLICABLE
from edcs_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edcs_identifier.subject_identifier import (
    SubjectIdentifier as BaseSubjectIdentifier,
)
from edcs_model.models import BaseUuidModel, HistoricalRecords, OtherCharField
from edcs_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edcs_screening.choices import CLINIC, PATIENT_CATEGORY
from edcs_search.model_mixins import SearchSlugManager
from edcs_sites.models import SiteModelMixin
from edcs_utils import get_utcnow

from ..choices import IDENTITY_TYPE
from ..model_mixins import SearchSlugModelMixin


class SubjectIdentifier(BaseSubjectIdentifier):
    template = "{protocol_number}-{site_id}-{sequence}"
    padding = 4


class SubjectConsentManager(SearchSlugManager, models.Manager):
    def get_by_natural_key(self, subject_identifier, version):
        return self.get(subject_identifier=subject_identifier, version=version)


class SubjectConsent(
    ConsentModelMixin,
    SiteModelMixin,
    UpdatesOrCreatesRegistrationModelMixin,
    NonUniqueSubjectIdentifierModelMixin,
    IdentityFieldsMixin,
    ReviewFieldsMixin,
    PersonalFieldsMixin,
    SampleCollectionFieldsMixin,
    CitizenFieldsMixin,
    VulnerabilityFieldsMixin,
    SearchSlugModelMixin,
    BaseUuidModel,
):
    """A model completed by the user that captures the ICF."""

    subject_identifier_cls = SubjectIdentifier

    subject_screening_model = "edcs_screening.subjectscreening"

    screening_identifier = models.CharField(
        verbose_name="Screening identifier",
        max_length=50,
        unique=True,
        help_text="(readonly)",
    )

    screening_datetime = models.DateTimeField(
        verbose_name="Screening datetime", null=True, editable=False
    )

    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected?",
        max_length=45,
        choices=CLINIC,
        null=True,
    )

    patient_category = models.CharField(
        verbose_name="Patient Category?",
        max_length=45,
        null=True,
        choices=PATIENT_CATEGORY,
    )

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,
        blank=False,
    )

    nationality = models.CharField(
        verbose_name="Nationality", max_length=60, choices=COUNTRY
    )

    nationality_other = OtherCharField()

    identity_type = models.CharField(
        verbose_name="What type of identity number is this?",
        max_length=25,
        choices=IDENTITY_TYPE,
    )

    objects = SubjectConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.subject_identifier} V{self.version}"

    def save(self, *args, **kwargs):
        subject_screening = self.get_subject_screening()
        self.screening_datetime = subject_screening.report_datetime
        self.subject_type = "subject"
        self.is_verified = True
        self.is_verified_datetime = get_utcnow()
        # self.verified_by = self.user.username
        self.citizen = NOT_APPLICABLE
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_subject_screening(self):
        """Returns the subject screening model instance.

        Instance must exist since SubjectScreening is completed
        before consent.
        """
        model_cls = django_apps.get_model(self.subject_screening_model)
        return model_cls.objects.get(screening_identifier=self.screening_identifier)

    @property
    def registration_unique_field(self):
        """Required for UpdatesOrCreatesRegistrationModelMixin."""
        return "subject_identifier"

    class Meta(ConsentModelMixin.Meta):
        unique_together = (
            ("subject_identifier", "version"),
            ("subject_identifier", "screening_identifier"),
            ("first_name", "dob", "initials", "version"),
        )

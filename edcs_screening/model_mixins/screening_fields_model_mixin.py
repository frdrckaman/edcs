from uuid import uuid4

from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edcs_constants.choices import GENDER, YES_NO, YES_NO_NA
from edcs_constants.constants import NO, NOT_APPLICABLE
from edcs_model.models.historical_records import HistoricalRecords
from edcs_sites.models import CurrentSiteManager, SiteModelMixin
from edcs_utils.date import get_utcnow

# from edcs_search.model_mixins import SearchSlugManager


class ScreeningManager(models.Manager):

    use_in_migrations = True

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class ScreeningFieldsModeMixin(SiteModelMixin, models.Model):
    reference = models.UUIDField(
        verbose_name="Reference", unique=True, default=uuid4, editable=False
    )

    screening_identifier = models.CharField(
        verbose_name="Screening ID",
        max_length=50,
        blank=True,
        unique=True,
        editable=False,
    )

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    gender = models.CharField(choices=GENDER, max_length=10)

    age_in_years = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(110)],
        help_text="Estimated age  in years if patient doesn’t know",
    )

    eligible = models.BooleanField(default=False, editable=False)

    reasons_ineligible = models.TextField(
        verbose_name="Reason not eligible", max_length=150, null=True, editable=False
    )

    eligibility_datetime = models.DateTimeField(
        null=True, editable=False, help_text="Date and time eligibility was determined"
    )

    consented = models.BooleanField(default=False, editable=False)

    refused = models.BooleanField(default=False, editable=False)

    on_site = CurrentSiteManager()

    objects = ScreeningManager()

    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

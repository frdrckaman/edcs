from django.db import models
from django_crypto_fields.fields import EncryptedTextField

from edcs_constants.choices import YES_NO
from edcs_crf.crf_model_mixins import CrfModelMixin
from edcs_model import models as edcs_models
from edcs_model.models import OtherCharField, date_not_future, datetime_not_future
from edcs_utils import get_utcnow

from ..choices import DEATH_LOCATIONS, INFORMANT_RELATIONSHIP


class DeathReport(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[datetime_not_future],
        default=get_utcnow,
    )

    death_date = models.DateField(
        validators=[date_not_future],
        verbose_name="Date of Death",
        null=True,
        blank=False,
    )

    death_location = models.CharField(
        verbose_name="Where did the participant die?",
        max_length=50,
        choices=DEATH_LOCATIONS,
    )

    # TODO: if hospital of clinic, require, else NA
    hospital_name = models.CharField(
        verbose_name=(
            "If death occurred at hospital / clinic, please give name of the facility"
        ),
        max_length=150,
        null=True,
        blank=True,
    )

    informant_contact = EncryptedTextField(null=True, blank=True)

    informant_relationship = models.CharField(
        max_length=50,
        choices=INFORMANT_RELATIONSHIP,
        verbose_name="Informants relationship to the participant?",
    )

    other_informant_relationship = OtherCharField()

    death_certificate = models.CharField(
        verbose_name="Is a death certificate is available?",
        max_length=15,
        choices=YES_NO,
    )

    cause_of_death = models.CharField(
        verbose_name="Main cause of death",
        max_length=180,
        help_text=(
            "Main cause of death in the opinion of the " "local study doctor and local PI"
        ),
    )

    cause_of_death_other = OtherCharField(max_length=100, blank=True, null=True)

    secondary_cause_of_death = models.CharField(
        verbose_name="Secondary cause of death",
        max_length=180,
        help_text=(
            "Secondary cause of death in the opinion of the " "local study doctor and local PI"
        ),
    )

    secondary_cause_of_death_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If "Other" above, please specify',
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Death Report"
        verbose_name_plural = "Death Report"

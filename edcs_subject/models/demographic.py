from django.db import models

from edcs_constants.choices import MARITAL_STATUS
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import EDUCATION, OCCUPATION
from ..model_mixins import CrfModelMixin


class DemographicCharacteristic(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )
    martial_status = models.CharField(
        verbose_name="Marital status?",
        max_length=45,
        choices=MARITAL_STATUS,
    )

    education = models.CharField(
        verbose_name="Education level?",
        max_length=45,
        choices=EDUCATION,
    )

    education_other = edcs_models.OtherCharField()

    occupation = models.CharField(
        verbose_name="Occupation",
        max_length=45,
        choices=OCCUPATION,
    )

    # new field
    occupation_details = models.CharField(
        verbose_name="Provide more details about the above occupation?",
        max_length=85,
        blank=True,
        null=True,
    )

    # new field
    occupation_duration = models.DecimalField(
        verbose_name="How long have you been working on the above occupation?",
        null=True,
        max_digits=6,
        decimal_places=3,
        help_text="Three month = 0.25, Six month = 0.5, One year = 1 , year and six month = "
        "1.5 etc.",
    )

    occupation_other = edcs_models.OtherCharField()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Demographic"
        verbose_name_plural = "Demographic"

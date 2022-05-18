from django.db import models

from edcs_model import models as edcs_models
from edcs_model.models import datetime_not_future
from edcs_utils import get_utcnow

from ..choices import BIOPSY_SIDE, BIOPSY_SITE
from ..model_mixins import CrfModelMixin


class LabPartB(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text="Date and time of report.",
    )

    side_biopsy_taken = models.CharField(
        verbose_name="Side of the body where the biopsy was taken",
        choices=BIOPSY_SIDE,
        max_length=45,
        blank=False,
        null=False,
    )

    location_site = models.CharField(
        verbose_name="Location/site?",
        max_length=45,
        choices=BIOPSY_SITE,
    )

    nature_of_specimen = models.TextField(
        verbose_name="Nature of specimen (Tissue or Fluid)",
        max_length=500,
    )

    xray_findings = models.TextField(
        verbose_name="X-ray findings",
        max_length=500,
    )

    ct_findings = models.TextField(
        verbose_name="CT findings",
        max_length=500,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lab Part B"
        verbose_name_plural = "Lab Part B"

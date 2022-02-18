from django.db import models

from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin
from ..choices import QN103, QN105


class LungCancerTreatment(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    lung_cancer_stage = models.CharField(
        verbose_name="What is the stage of lung cancer?",
        max_length=45,
        choices=QN103,
        default=NOT_APPLICABLE
    )

    date_start_treatment = models.DateField(
        verbose_name="Date started Treatment?",
        max_length=45,
        null=True,
        blank=True,
    )

    treatment = models.CharField(
        verbose_name="Type of treatment?",
        max_length=45,
        choices=QN105,
        default=NOT_APPLICABLE
    )

    treatment_other = edcs_models.OtherCharField()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lung Cancer Treatment"
        verbose_name_plural = "Lung Cancer Treatment"

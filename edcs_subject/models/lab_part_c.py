from django.db import models

from edcs_constants.choices import POS_NEG_ONLY
from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edcs_models
from edcs_model.models import datetime_not_future
from edcs_utils import get_utcnow

from ..choices import IMM_HIST_CHEM_UP, NON_SMALL_CELL, TYPE_LUNG_CA
from ..model_mixins import CrfModelMixin


class LabPartC(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text="Date and time of report.",
    )

    histological_dx = models.TextField(
        verbose_name="Histological diagnosis",
    )

    measurements = models.TextField(
        verbose_name="Measurements",
    )

    consistency = models.TextField(
        verbose_name="Consistency",
        max_length=500,
    )

    color = models.CharField(
        verbose_name="Color",
        max_length=45,
    )

    microscopic_findings = models.TextField(
        verbose_name="Microscopic findings",
        max_length=500,
    )

    immunohistochemistry = models.CharField(
        verbose_name="Immunohistochemistry",
        max_length=45,
        choices=IMM_HIST_CHEM_UP,
    )

    histochemistry = models.CharField(
        verbose_name="Histochemistry",
        max_length=45,
        choices=IMM_HIST_CHEM_UP,
    )

    type_lung_ca = models.CharField(
        verbose_name="Type of lung Cancer?",
        max_length=45,
        choices=TYPE_LUNG_CA,
    )

    non_small_cell = models.CharField(
        verbose_name="If non-small cell",
        max_length=45,
        choices=NON_SMALL_CELL,
        default=NOT_APPLICABLE,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lab Part C"
        verbose_name_plural = "Lab Part C"

from django.db import models

from edcs_constants.choices import POS_NEG_NA, POS_NEG_ONLY
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import HIVSubtype, SomaticMutations
from edcs_model import models as edcs_models
from edcs_model.models import datetime_not_future
from edcs_utils import get_utcnow

from ..choices import HIV_DRUG_RESISTANCE
from ..model_mixins import CrfModelMixin


class LabPartD(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text="Date and time of report.",
    )

    hiv_dna_pcr = models.TextField(
        verbose_name="HIV DNA PCR",
        choices=POS_NEG_NA,
        default=NOT_APPLICABLE,
    )

    hiv_subtype = models.ManyToManyField(
        HIVSubtype,
        verbose_name="HIV subtype",
    )

    somatic_mutations = models.ManyToManyField(
        SomaticMutations,
        verbose_name="Somatic mutations ",
    )

    dna_methylation = models.CharField(
        verbose_name="DNA methylation age",
        max_length=45,
    )

    hiv_drug_resistance_test = models.TextField(
        verbose_name="HIV drug resistance",
        max_length=45,
        choices=HIV_DRUG_RESISTANCE,
        default=NOT_APPLICABLE,
    )

    hiv_drug_resistance_other = edcs_models.OtherCharField()

    hiv_current_regimen = models.CharField(
        verbose_name="Current Regimen",
        max_length=125,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lab Part D"
        verbose_name_plural = "Lab Part D"

from django.db import models

from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin


class LungCancerLabInvestigation(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    biopsy_tissues_mutation = models.CharField(
        verbose_name="From the biopsy tissues, is there any mutation?",
        max_length=45,
        choices=YES_NO,
    )

    mutation_detected = models.CharField(
        verbose_name="If yes, what mutations were detected?",
        max_length=125,
        blank=True,
        null=True,
    )

    dna_methylation_age = models.CharField(
        verbose_name="Was the DNA methylation age done?", max_length=45, choices=YES_NO
    )

    dna_methylation_result = models.CharField(
        verbose_name="If yes, what were the DNAm results?",
        max_length=125,
        blank=True,
        null=True,
    )

    brock_score = models.CharField(
        verbose_name="What was the patient’s Brock score?",
        max_length=45,
        blank=True,
        null=True,
    )
    lungrads_score = models.CharField(
        verbose_name="What was the patient’s LungRADS score?",
        max_length=45,
        blank=True,
        null=True,
    )
    luniris_score = models.CharField(
        verbose_name="What was the patient’s LunIRiS score?",
        max_length=45,
        blank=True,
        null=True,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lung Cancer Lab Investigation"
        verbose_name_plural = "Lung Cancer Lab Investigation"

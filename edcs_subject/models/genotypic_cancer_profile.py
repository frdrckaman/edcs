from django.db import models

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin


class GenotypicCancerProfile(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    sample_type = models.CharField(
        verbose_name="Sample Type",
        max_length=20,
        null=True,
    )

    date_received = models.DateTimeField(
        verbose_name="Date Received",
    )

    cancer_type = models.CharField(
        verbose_name="Cancer Type",
        max_length=45,
    )

    genomic_alteration = models.CharField(
        verbose_name="Genomic Alteration",
        max_length=45,
        null=True,
    )

    allele_frequency = models.DecimalField(
        verbose_name="Allele Frequency",
        decimal_places=2,
        max_digits=4,
        null=True,
        help_text="Percentage %",
    )

    variant_class = models.CharField(
        verbose_name="Variant Class",
        max_length=45,
    )

    coverage = models.IntegerField(
        verbose_name="Coverage",
    )

    biomarker_this_cancer = models.TextField(
        verbose_name="Biomarker-based Relevant Therapies",
        blank=True,
        null=True,
        help_text="In this cancer type",
    )

    biomarker_other_cancer = models.TextField(
        verbose_name="Biomarker-based Relevant Therapies",
        blank=True,
        null=True,
        help_text="In other cancer type",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Genotypic Cancer Profile"
        verbose_name_plural = "Genotypic Cancer Profile"

from django.db import models

from edcs_lists.models import OncomineVariantClass
from edcs_model import models as edcs_models
from edcs_subject.models import SubjectVisit
from edcs_utils import get_utcnow

from ..choices import ASSAY_STATUS
from ..model_mixins import CrfModelMixin

ID = (("", "------------"),)


class Genotypic(edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    assay_status = models.CharField(
        verbose_name="Assay Status",
        max_length=45,
        null=True,
        choices=ASSAY_STATUS,
    )

    oncomine_variant = models.ManyToManyField(
        OncomineVariantClass, verbose_name="Oncomine Variant Class", null=True
    )

    gene = models.CharField(
        verbose_name="Gene",
        max_length=45,
        blank=True,
        null=True,
    )

    genotype = models.TextField(verbose_name="Genotype", blank=True, null=True)

    amino_acid_change = models.TextField(
        verbose_name="Amino Acid Change", blank=True, null=True
    )

    coverage = models.IntegerField(verbose_name="Coverage", blank=True, null=True)

    allele_frequency = models.DecimalField(
        verbose_name="Allele Frequency", max_digits=6, decimal_places=2, blank=True, null=True
    )

    sample_type = models.CharField(
        verbose_name="Sample Type",
        max_length=20,
        blank=True,
        null=True,
    )

    date_received = models.DateTimeField(
        verbose_name="Date Received",
        blank=True,
        null=True,
    )

    cancer_type = models.CharField(
        verbose_name="Cancer Type",
        max_length=45,
        blank=True,
        null=True,
    )

    genomic_alteration = models.CharField(
        verbose_name="Genomic Alteration",
        max_length=45,
        blank=True,
        null=True,
    )

    variant_class = models.CharField(
        verbose_name="Variant Class",
        max_length=45,
        blank=True,
        null=True,
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

    subject_visit = models.ForeignKey(
        SubjectVisit,
        verbose_name="Subject Visit",
        on_delete=models.CASCADE,
        related_name="genotypic",
        null=True,
    )
    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=45,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Genotypic Cancer Profile"
        verbose_name_plural = "Genotypic Cancer Profile"

from django.db import models
from django.utils import timezone

from edcs_model import models as edcs_models
from edcs_subject.models import LungCancerTreatment

from ..choices import CHEMOTHERAPY_DRUG


class ChemotherapyDrugs(edcs_models.BaseUuidModel):
    lung_cancer_treatment = models.ForeignKey(
        LungCancerTreatment,
        on_delete=models.CASCADE,
        related_name="chemotherapy_drugs",
    )

    chemotherapy_drug = models.CharField(
        verbose_name="Chemotherapy Drug",
        max_length=45,
        choices=CHEMOTHERAPY_DRUG,
    )

    number_of_cycles = models.IntegerField(
        verbose_name="Number of cycles",
    )

    timestamp = models.DateTimeField(
        verbose_name="Timestamp",
        default=timezone.now,
    )

    history = edcs_models.HistoricalRecords()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Chemotherapy Drug"
        verbose_name_plural = "Chemotherapy Drugs"

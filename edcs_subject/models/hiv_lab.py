from django.db import models

from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models

from ..choices import QN103, QN106, QN110


class HivLabInvestigation(
    edcs_models.BaseUuidModel,
):

    hiv_status = models.CharField(
        verbose_name="If the patient’s status is unknown or Negative, tested more than two months ago, please counsel "
        "the patient (Provider initiated HIV counseling and testing) and take blood for HIV testing.",
        max_length=45,
        choices=QN106,
    )

    baseline_cd4 = models.IntegerField(
        verbose_name="Baseline CD4 counts",
        max_length=45,
    )

    baseline_viral_load = models.IntegerField(
        verbose_name="Baseline Viral Load",
        max_length=45,
    )

    hiv_stage = models.CharField(
        verbose_name="What is the patient HIV stage?",
        max_length=45,
        choices=QN103,
    )

    hiv_subtype_done = models.CharField(
        verbose_name="Was the patient’s HIV subtype done?",
        max_length=45,
        choices=YES_NO,
    )
    hiv_subtype = models.CharField(
        verbose_name="Was the patient’s HIV subtype done?",
        max_length=45,
        choices=QN110,
    )
    drug_resistance_testing_done = models.CharField(
        verbose_name="Was the patient’s HIV subtype done?",
        max_length=45,
        choices=YES_NO,
    )
    drug_resistance = models.CharField(
        verbose_name="If yes, what is the patient’s HIV drug resistance results?",
        max_length=125,
        blank=True,
        null=True,
    )

    treatment_other = edcs_models.OtherCharField()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Hiv Lab Investigation"
        verbose_name_plural = "Hiv Lab Investigation"

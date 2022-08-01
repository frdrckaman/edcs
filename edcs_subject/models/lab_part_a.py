from django.db import models

from edcs_constants.choices import POS_NEG
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import TB_TEST_TYPE, TEST_RESULTS
from ..model_mixins import CrfModelMixin


# TODO put hint on form eg (copies/mL)
class LabPartA(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    hiv_rapid_test = models.CharField(
        verbose_name="HIV rapid test",
        choices=TEST_RESULTS,
        max_length=45,
        blank=False,
        null=False,
    )

    type_tb_test = models.CharField(
        verbose_name="Type of TB Test Done?",
        max_length=45,
        choices=TB_TEST_TYPE,
    )

    type_tb_test_other = edcs_models.OtherCharField()

    tb_test_result = models.CharField(
        verbose_name="TB Test Results?",
        max_length=45,
        choices=POS_NEG,
    )

    baseline_cd4_counts = models.IntegerField(
        verbose_name="Baseline CD4 counts",
        null=True,
        blank=True,
    )
    # TODO put viral load on prn form for 6m - 60m
    baseline_viral_load = models.IntegerField(
        verbose_name="Baseline Viral Load",
        null=True,
        blank=True,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Lab Part A"
        verbose_name_plural = "Lab Part A"

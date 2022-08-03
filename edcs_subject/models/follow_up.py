from django.db import models

from edcs_constants.choices import POS_NEG, YES_NO
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import FOLLOW_UP_TEST, PATIENT_STATUS_VISIT
from ..model_mixins import CrfModelMixin


class FollowUp(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    test_ordered = models.CharField(
        verbose_name="Have any test been ordered at this visit",
        choices=FOLLOW_UP_TEST,
        max_length=45,
        blank=False,
        null=False,
    )

    test_ordered_other = edcs_models.OtherCharField()

    test_ordered_result = models.TextField(
        verbose_name="If yes, provide the results",
        null=True,
        blank=True,
    )

    hiv_status = models.CharField(
        verbose_name="What is the patient's HIV status?",
        max_length=45,
        choices=POS_NEG,
    )

    viral_load_cd4_off = models.IntegerField(
        verbose_name="If positive, was the blood sample for viral load and CD4 count off?",
        null=True,
        blank=True,
    )

    current_viral_load = models.IntegerField(
        verbose_name="What is current Viral Load level",
        null=True,
        blank=True,
    )
    current_cd4_count = models.IntegerField(
        verbose_name="What is current CD4 count",
        null=True,
        blank=True,
    )

    hiv_genotype = models.CharField(
        verbose_name="Was the patient's HIV genotype done?",
        max_length=15,
        choices=YES_NO,
    )

    patient_visit_status = models.CharField(
        verbose_name="What is the patient status at this visit?",
        max_length=45,
        choices=PATIENT_STATUS_VISIT,
    )

    respond_treatment = models.CharField(
        verbose_name="If the patient is not responding to treatment, has the patient's "
        "treatment changed?",
        max_length=15,
        choices=YES_NO,
    )

    treatment_change = models.TextField(
        verbose_name="If yes specify",
        null=True,
        blank=True,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Follow Up"
        verbose_name_plural = "Follow Up"

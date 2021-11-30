from django.db import models
from django.utils.safestring import mark_safe

from edcs_constants.choices import (
    HIV_RESULT_DWTA_DONT_KNOW,
    YES_NO,
    YES_NO_DECLINED_TO_ANSWER,
    YES_NO_DWTA_DONT_KNOW,
)
from edcs_crf.crf_model_mixins import CrfModelMixin
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import LUNG_DISEASE, MISS_ARV, QN100, QN101, QN102


class ClinicalReview(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    hiv_test = models.CharField(
        verbose_name="Have you ever been tested for HIV?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    hiv_test_date = models.DateField(
        verbose_name="If yes, when was your most recent HIV test?",
        null=True,
        blank=True,
    )

    hiv_dx = models.CharField(
        verbose_name=mark_safe("What was the result of your most recent HIV test?"),
        max_length=45,
        choices=HIV_RESULT_DWTA_DONT_KNOW,
        default=None,
    )
    arv = models.CharField(
        verbose_name=mark_safe("If positive, are you taking ARVs?"),
        max_length=45,
        choices=HIV_RESULT_DWTA_DONT_KNOW,
        default=None,
    )

    arv_start_date = models.DateField(
        verbose_name="Month and year patient started taking ARVs?",
        null=True,
        blank=True,
    )

    arv_regularly = models.CharField(
        verbose_name=mark_safe("Do you take your ARVs regularly? "),
        max_length=15,
        choices=YES_NO,
        default=None,
    )

    miss_taking_arv = models.CharField(
        verbose_name=mark_safe("If no, how often do you miss taking ARVs?"),
        max_length=45,
        choices=MISS_ARV,
        default=None,
    )

    miss_taking_arv_other = edcs_models.OtherCharField()

    lung_diseases_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with a chronic lung disease like Asthma, COPD, and Interstitial "
        "lung disease?",
        max_length=45,
        choices=LUNG_DISEASE,
    )

    lung_diseases_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_lung_diseases_medication = models.CharField(
        verbose_name="Are you using any medications?",
        choices=YES_NO_DECLINED_TO_ANSWER,
        max_length=80,
        default=None,
    )

    lung_diseases_medication = models.TextField(
        verbose_name="If is yes, what medications are you using?",
        null=True,
        blank=True,
    )

    htn_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=45,
        choices=YES_NO,
    )

    htn_dx_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_htn_medication = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    htn_medication = models.TextField(
        verbose_name="If is yes, what medications are you using currently?",
        null=True,
        blank=True,
    )

    dm_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with have Diabetes Mellitus? ",
        max_length=15,
        choices=YES_NO,
    )

    dm_dx_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_dm_medication = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    dm_medication = models.TextField(
        verbose_name="If is yes, what medications are you using currently?",
        null=True,
        blank=True,
    )

    malignancy = models.CharField(
        verbose_name="Have you ever had any other malignancy?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    tb_test = models.CharField(
        verbose_name="Were you tested for TB?",
        max_length=45,
        choices=YES_NO,
    )

    provide_sputum_tb_dx = models.CharField(
        verbose_name="If No, has the patient provided sputum for TB diagnosis?",
        max_length=45,
        choices=QN100,
    )

    tb_status = models.CharField(
        verbose_name="What is the patients TB status?",
        max_length=45,
        choices=QN101,
    )

    lung_cancer_dx = models.CharField(
        verbose_name="What is the patient’s lung cancer diagnosis?",
        max_length=45,
        choices=QN102,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Clinical Review"
        verbose_name_plural = "Clinical Reviews"

from django.db import models
from django.utils.safestring import mark_safe
from edcs_constants.choices import YES_NO, YES_NO_DWTA_DONT_KNOW, HIV_RESULT_DWTA_DONT_KNOW, YES_NO_DECLINED_TO_ANSWER
from edcs_model import models as edcs_models
from ..choices import MISS_ARV, LUNG_DISEASE


class ClinicalReview(
    edcs_models.BaseUuidModel,
):

    hiv_test = models.CharField(
        verbose_name="Have you ever been tested for HIV?",
        max_length=15,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    hiv_test_date = models.DateField(
        verbose_name="If yes, when was your most recent HIV test?",
        null=True,
        blank=True,
    )

    hiv_dx = models.CharField(
        verbose_name=mark_safe(
            "What was the result of your most recent HIV test?"
        ),
        max_length=15,
        choices=HIV_RESULT_DWTA_DONT_KNOW,
        null=True,
        blank=True,
    )
    arv = models.CharField(
        verbose_name=mark_safe(
            "If positive, are you taking ARVs?"
        ),
        max_length=15,
        choices=HIV_RESULT_DWTA_DONT_KNOW,
        null=True,
        blank=True,
    )

    arv_start_date = models.DateField(
        verbose_name="Month and year patient started taking ARVs?",
        null=True,
        blank=True,
    )

    arv_regularly = models.CharField(
        verbose_name=mark_safe(
            "Do you take your ARVs regularly? "
        ),
        max_length=15,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    miss_taking_arv = models.CharField(
        verbose_name=mark_safe(
            "If no, how often do you miss taking ARVs?"
        ),
        max_length=15,
        choices=MISS_ARV,
        null=True,
        blank=True,
    )

    miss_taking_arv_other = edcs_models.OtherCharField()

    lung_diseases_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with a chronic lung disease like Asthma, COPD, and Interstitial "
                     "lung disease?",
        max_length=15,
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
        null=True,
        blank=True,
    )

    lung_diseases_medication = models.TextField(
        verbose_name="If is yes, what medications are you using?",
        null=True,
        blank=True,
    )

    htn_dx = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=15,
        choices=YES_NO,
    )

    htn_dx_date = models.DateField(
        verbose_name="If yes, when were you diagnosed?",
        null=True,
        blank=True,
    )

    use_htn_medication = models.CharField(
        verbose_name="Have you ever been diagnosed with Hypertension?",
        max_length=15,
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
        max_length=15,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    dm_medication = models.TextField(
        verbose_name="If is yes, what medications are you using currently?",
        null=True,
        blank=True,
    )

    malignancy = models.CharField(
        verbose_name="If is yes, what medications are you using currently?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Clinical Review"
        verbose_name_plural = "Clinical Reviews"

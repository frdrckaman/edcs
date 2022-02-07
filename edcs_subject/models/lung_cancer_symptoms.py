from django.db import models

from edcs_constants.choices import YES_NO_DWTA_DONT_KNOW, YES_NO_DECLINED_TO_ANSWER
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin
from ..choices import QN90, QN91, QN92, QN94, QN95, QN98, QN102


class SignSymptomLungCancer(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    what_brought_hospital = models.CharField(
        verbose_name="What brought you to the hospital that made the doctors suspect/diagnose you to have lung cancer?",
        max_length=45,
        choices=QN90,
    )

    what_brought_hospital_other = edcs_models.OtherCharField()

    symptoms_how_long = models.CharField(
        verbose_name="For how long have you been sick with the above symptoms?",
        max_length=45,
        choices=QN91,
    )

    characterize_symptoms = models.CharField(
        verbose_name="How would you characterize your symptoms?",
        max_length=45,
        choices=QN92,
    )

    family_member_same_symptoms = models.CharField(
        verbose_name="Has anyone else in the family presented with the same symptoms?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    family_member_relationship = models.CharField(
        verbose_name="If yes, what is your relationship with the above-mentioned person?",
        max_length=45,
        choices=QN94,
    )
    chest_radiation = models.CharField(
        verbose_name="",
        max_length=45,
        null=True,
        choices=YES_NO_DECLINED_TO_ANSWER
    )

    no_chest_radiation = models.IntegerField(
        verbose_name="If yes, how many times?"
    )
    # family_member_dx_cancer = models.CharField(
    #     verbose_name="Has any member of your family been diagnosed with either breast cancer, colon cancer, "
    #     "lung cancer, ovarian cancer, prostate cancer, thyroid or uterine cancer?",
    #     max_length=45,
    #     choices=QN95,
    # )
    time_take_referred_cancer_facilities = models.IntegerField(
        verbose_name="From the very first time you sought care from the health facility to the time you were"
        " referred to the cancer treatment facility, how long did it take?",
        help_text="(Ask the patient to show you his/her referral documents. Duration in days)",
    )

    investigations_ordered = models.DateField(
        verbose_name="While at cancer treatment facility, what investigations did the doctor(s) order?",
        max_length=45,
        choices=QN98,
    )

    non_investigations_ordered = models.TextField(
        verbose_name="If none, state reason why?", blank=True, null=True
    )

    lung_cancer_dx = models.CharField(
        verbose_name="What is the patient’s lung cancer diagnosis?",
        max_length=45,
        choices=QN102,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Sign Symptoms Lung Cancer"
        verbose_name_plural = "Sign Symptoms Lung Cancer"

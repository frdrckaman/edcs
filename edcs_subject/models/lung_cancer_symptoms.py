from django.db import models

from edcs_constants.choices import YES_NO_DECLINED_TO_ANSWER, YES_NO_DWTA_DONT_KNOW
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import CancerInvestigation, LungCancerSymptoms
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN90, QN91, QN92, QN94, QN95, QN98, QN102
from ..model_mixins import CrfModelMixin


class SignSymptomLungCancer(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    what_brought_hospital = models.ManyToManyField(
        LungCancerSymptoms,
        verbose_name="What brought you to the hospital that made the doctors suspect/diagnose you to have lung cancer?",
        related_name="lung_cancer_symptoms",
    )

    what_brought_hospital_other = edcs_models.OtherCharField()

    symptoms_how_long = models.CharField(
        verbose_name="For how long have you been sick with the above symptoms?",
        max_length=45,
        choices=QN91,
    )

    symptoms_greater_than_6months = models.CharField(
        verbose_name="If greater than 6 months, Please specify",
        max_length=45,
        null=True,
        blank=True,
    )

    characterize_symptoms = models.CharField(
        verbose_name="How would you characterize your symptoms?",
        max_length=45,
        choices=QN92,
    )

    characterize_symptoms_other = edcs_models.OtherCharField()

    family_member_same_symptoms = models.CharField(
        verbose_name="Has anyone else in the family presented with the same symptoms?",
        max_length=45,
        choices=YES_NO_DWTA_DONT_KNOW,
    )

    family_member_relationship = models.CharField(
        verbose_name="If yes, what is your relationship with the above-mentioned person?",
        max_length=45,
        choices=QN94,
        default=NOT_APPLICABLE,
    )

    family_member_relationship_other = edcs_models.OtherCharField()

    chest_radiation = models.CharField(
        verbose_name="Do you have history of chest radiation in the past 5 years?",
        max_length=45,
        null=True,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    no_chest_radiation = models.IntegerField(
        verbose_name="If yes, how many times?",
        null=True,
        blank=True,
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

    investigations_ordered = models.CharField(
        verbose_name="While at cancer treatment facility, what investigations did the doctor(s)"
        " order in relation to the illness?",
        max_length=45,
        choices=QN98,
        null=True,
    )

    investigations_ordered_nw = models.ManyToManyField(
        CancerInvestigation,
        verbose_name="While at cancer treatment facility, what investigations did the doctor(s)"
        " order in relation to the illness?",
    )

    investigations_ordered_other = edcs_models.OtherCharField()

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

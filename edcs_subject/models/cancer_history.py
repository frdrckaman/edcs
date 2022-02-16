from django.db import models
from edcs_constants.choices import YES_NO, YES_NO_NA
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import FamilyMembers
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN95
from ..model_mixins import CrfModelMixin


class CancerHistory(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    cancer_dx = models.CharField(
        verbose_name="Has any member of your close family been diagnosed with either breast cancer, colon cancer, "
                     "lung cancer, ovarian cancer, prostate cancer, thyroid or uterine cancer?",
        max_length=45,
        choices=QN95,
    )

    breast_cancer = models.CharField(
        verbose_name="Breast Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )
    #TODO age must not be -ve
    breast_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    breast_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="breast_cancer_family_member",
        blank=True,
    )

    breast_cancer_family_member_other = edcs_models.OtherCharField()

    colon_cancer = models.CharField(
        verbose_name="Colon Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    colon_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    colon_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="colon_cancer_family_member",
        blank=True,
    )

    colon_cancer_family_member_other = edcs_models.OtherCharField()

    lung_cancer = models.CharField(
        verbose_name="Lung Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    lung_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    lung_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="lung_cancer_family_member",
        blank=True,
    )

    lung_cancer_family_member_other = edcs_models.OtherCharField()

    ovarian_cancer = models.CharField(
        verbose_name="Ovarian Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    ovarian_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    ovarian_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="ovarian_cancer_family_member",
        blank=True,
    )

    ovarian_cancer_family_member_other = edcs_models.OtherCharField()

    prostate_cancer = models.CharField(
        verbose_name="Prostate Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    prostate_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    prostate_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="prostate_cancer_family_member",
        blank=True,
    )

    prostate_cancer_family_member_other = edcs_models.OtherCharField()

    thyroid_cancer = models.CharField(
        verbose_name="Thyroid Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    thyroid_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    thyroid_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="thyroid_cancer_family_member",
        blank=True,
    )

    thyroid_cancer_family_member_other = edcs_models.OtherCharField()

    uterine_cancer = models.CharField(
        verbose_name="Uterine Cancer",
        max_length=25,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE
    )

    uterine_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
        null=True,
        blank=True,
    )

    uterine_cancer_family_member = models.ManyToManyField(
        FamilyMembers,
        verbose_name="What is your relationship?",
        related_name="uterine_cancer_family_member",
        blank=True,
    )

    uterine_cancer_family_member_other = edcs_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Cancer History"
        verbose_name_plural = "Cancer History"

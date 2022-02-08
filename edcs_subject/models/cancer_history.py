from django.db import models
from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN95, FAMILY_MEMBERS
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
        choices=YES_NO,
        default=None
    )

    breast_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    breast_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    breast_cancer_family_member_other = edcs_models.OtherCharField()

    colon_cancer = models.CharField(
        verbose_name="Colon Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    colon_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    colon_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    colon_cancer_family_member_other = edcs_models.OtherCharField()

    lung_cancer = models.CharField(
        verbose_name="Lung Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    lung_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    lung_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    lung_cancer_family_member_other = edcs_models.OtherCharField()

    ovarian_cancer = models.CharField(
        verbose_name="Ovarian Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    ovarian_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    ovarian_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    ovarian_cancer_family_member_other = edcs_models.OtherCharField()

    prostate_cancer = models.CharField(
        verbose_name="Prostate Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    prostate_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    prostate_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    prostate_cancer_family_member_other = edcs_models.OtherCharField()

    thyroid_cancer = models.CharField(
        verbose_name="Thyroid Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    thyroid_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    thyroid_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    thyroid_cancer_family_member_other = edcs_models.OtherCharField()

    uterine_cancer = models.CharField(
        verbose_name="Uterine Cancer",
        max_length=25,
        choices=YES_NO,
        default=None
    )

    uterine_cancer_age_dx = models.IntegerField(
        verbose_name="Indicate age of diagnosis",
    )

    uterine_cancer_family_member = models.CharField(
        verbose_name="What is your relationship?",
        max_length=45,
        null=True,
        choices=FAMILY_MEMBERS,
        default=None,
    )

    uterine_cancer_family_member_other = edcs_models.OtherCharField()

    class Meta(CrfModelMixin.Meta, edcs_models.BaseUuidModel.Meta):
        verbose_name = "Cancer History"
        verbose_name_plural = "Cancer History"

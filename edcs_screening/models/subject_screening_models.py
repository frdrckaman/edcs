from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.db import models
from django_crypto_fields.fields import EncryptedCharField

from edcs_constants.choices import COUNTRY, YES_NO
from edcs_model.models import BaseUuidModel, OtherCharField
from edcs_screening.model_mixins import ScreeningModelMixin
from edcs_screening.screening_identifier import ScreeningIdentifier

from ..choices import CLINIC, PATIENT_CATEGORY
from ..eligibility import check_eligible_final


class SubjectScreeningModelError(Exception):
    pass


class ScreeningIdentifier(ScreeningIdentifier):
    template = "S{random_string}"


class SubjectScreening(
    ScreeningModelMixin,
    BaseUuidModel,
):
    identifier_cls = ScreeningIdentifier

    clinic_type = models.CharField(
        verbose_name="From which type of clinic was the patient selected?",
        max_length=45,
        choices=CLINIC,
    )

    patient_category = models.CharField(
        verbose_name="Patient Category?", max_length=45, choices=PATIENT_CATEGORY
    )

    screening_consent = models.CharField(
        verbose_name=(
            "Has the subject given his/her verbal consent "
            "to be screened for the U54 Lung Cancer Study?"
        ),
        max_length=15,
        choices=YES_NO,
    )
    nationality = models.CharField(
        verbose_name="Nationality", max_length=60, choices=COUNTRY
    )

    nationality_other = OtherCharField()

    region = models.CharField(
        verbose_name="Region:",
        max_length=50,
    )
    district = models.CharField(
        verbose_name="District:",
        max_length=50,
    )
    patient_know_dob = models.CharField(
        verbose_name="Does the patient know his/her date of birth?",
        choices=YES_NO,
        max_length=50,
    )
    patient_dob = models.DateField(
        verbose_name="What is patient date of birth?",
        null=True,
        blank=True,
    )
    hospital_id = EncryptedCharField(
        verbose_name="Patients hospital identification number:",
        max_length=50,
        blank=False,
    )
    initials = EncryptedCharField(
        validators=[
            RegexValidator("[A-Z]{1,3}", "Invalid format"),
            MinLengthValidator(2),
            MaxLengthValidator(3),
        ],
        help_text="Use UPPERCASE letters only. May be 2 or 3 letters.",
        blank=False,
    )
    """Exclusion criteria"""
    tb_diagnosis = models.CharField(
        verbose_name="Does the patient have a positive TB diagnosis?",
        max_length=25,
        choices=YES_NO,
    )
    """Exclusion criteria"""
    malignancy = models.CharField(
        verbose_name="Have you ever had any other malignancy? ",
        max_length=25,
        choices=YES_NO,
    )
    """Exclusion criteria"""
    above_eighteen = models.CharField(
        verbose_name="Is the patient 18 years and above?",
        max_length=25,
        choices=YES_NO,
    )
    persistent_breathlessness = models.CharField(
        verbose_name="Has the patient had persistent breathlessness?",
        max_length=25,
        choices=YES_NO,
    )
    persistent_tiredness = models.CharField(
        verbose_name="Has the patient had persistent tiredness or lack of energy?",
        max_length=25,
        choices=YES_NO,
    )
    wheezing = models.CharField(
        verbose_name="Has the patient been wheezing?",
        max_length=25,
        choices=YES_NO,
    )
    shortness_of_breath = models.CharField(
        verbose_name="Has the patient had shortness of breath?",
        max_length=25,
        choices=YES_NO,
    )
    weight_loss = models.CharField(
        verbose_name="Has the patient had unexplained weight loss?",
        max_length=25,
        choices=YES_NO,
    )
    abnormal_chest_xrays = models.CharField(
        verbose_name="Does the patient have abnormal chest x-rays demonstrating nodules and/or masses?",
        max_length=25,
        choices=YES_NO,
    )
    non_resolving_infection = models.CharField(
        verbose_name="Does the patient have non-resolving infection including tuberculosis?",
        max_length=25,
        choices=YES_NO,
    )

    lung_cancer_suspect = models.CharField(
        verbose_name="Has the patient been suspected to have lung cancer on the basis of clinical presentation?",
        max_length=25,
        choices=YES_NO,
    )
    cough = models.CharField(
        verbose_name="Has the patient had cough that doesn't go away after 2 or 3 weeks?",
        max_length=25,
        choices=YES_NO,
    )
    long_standing_cough = models.CharField(
        verbose_name="Has the patient had a long-standing cough that gets worse?",
        max_length=25,
        choices=YES_NO,
    )
    cough_blood = models.CharField(
        verbose_name="Has the patient been coughing up blood or rust-colored sputum (spit or phlegm)?",
        max_length=25,
        choices=YES_NO,
    )
    chest_infections = models.CharField(
        verbose_name="Has the patient had chest infections that keep coming back such as bronchitis, pneumonia?",
        max_length=25,
        choices=YES_NO,
    )
    chest_pain = models.CharField(
        verbose_name="Has the patient had chest pain that is often worsen when breathing or coughing?",
        max_length=25,
        choices=YES_NO,
    )
    """Exclusion criteria"""
    diagnosed_lung_cancer = models.CharField(
        verbose_name="Have you ever been diagnosed with lung cancer?",
        max_length=25,
        choices=YES_NO,
    )

    def save(self, *args, **kwargs):
        check_eligible_final(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Subject Screening"
        verbose_name_plural = "Subject Screening"

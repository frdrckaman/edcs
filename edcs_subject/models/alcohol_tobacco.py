from django.db import models

from edcs_constants.choices import YES_NO
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import SmokingTobaccoProducts, TobaccoProducts
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import (
    ALCOHOL_CONSUMPTION,
    ALCOHOL_CONSUMPTION_FREQUENCY,
    SMOKE_INSIDE,
    SMOKE_TOBACCO_PRODUCTS,
    SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
    TOBACCO_PRODUCTS,
)
from ..model_mixins import CrfModelMixin


class AlcoholTobaccoUse(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )
    smoke_chew_tobacco = models.ManyToManyField(
        SmokingTobaccoProducts, verbose_name="Do you smoke or chew tobacco products?"
    )
    tobacco_products = models.ManyToManyField(
        TobaccoProducts,
        verbose_name="If currently/past smoker/chew, which tobacco products do you/ did you smoke/chew.",
    )
    tobacco_products_other = edcs_models.OtherCharField()

    date_start_smoking = models.DateField(
        verbose_name="Month and Year Patient started smoking tobacco products",
        null=True,
        blank=True,
    )
    smoking_frequency = models.CharField(
        verbose_name="How frequently do you smoke these products?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
        default=NOT_APPLICABLE,
        null=True,
    )
    smoking_frequency_other = edcs_models.OtherCharField()

    # new field
    smoking_frequency_cigarettes = models.CharField(
        verbose_name="How frequently do you smoke cigarettes?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
        default=NOT_APPLICABLE,
    )
    # new field
    smoking_frequency_other_cigarettes = edcs_models.OtherCharField()

    # new field
    smoking_frequency_cigars = models.CharField(
        verbose_name="How frequently do you smoke cigars?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
        default=NOT_APPLICABLE,
    )

    # new field
    smoking_frequency_other_cigars = edcs_models.OtherCharField()

    # new field
    smoking_frequency_shisha = models.CharField(
        verbose_name="How frequently do you smoke shisha?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
        default=NOT_APPLICABLE,
    )

    # new field
    smoking_frequency_other_shisha = edcs_models.OtherCharField()

    # new field
    smoking_frequency_pipes = models.CharField(
        verbose_name="How frequently do you smoke pipes?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
        default=NOT_APPLICABLE,
    )

    # new field
    smoking_frequency_other_pipes = edcs_models.OtherCharField()

    # new field
    no_tobacco_product_smoked = models.IntegerField(
        verbose_name="On average, how many of these products do you/did you smoke?",
        null=True,
        blank=True,
    )

    # new field
    no_cigarettes_smoked = models.IntegerField(
        verbose_name="On average, how many Cigarettes do you/did you smoke?",
        null=True,
        blank=True,
    )

    # new field
    no_cigars_smoked = models.IntegerField(
        verbose_name="On average, how many Cigars do you/did you smoke?",
        null=True,
        blank=True,
    )

    # new field
    no_shisha_smoked = models.IntegerField(
        verbose_name="On average, how many Shisha do you/did you smoke?",
        null=True,
        blank=True,
    )

    # new field
    no_pipe_smoked = models.IntegerField(
        verbose_name="On average, how many Pipes do you/did you smoke?",
        null=True,
        blank=True,
    )
    age_start_smoking = models.IntegerField(
        verbose_name="If past/current smoker, at what age did you first start smoking?",
        help_text="in years",
        null=True,
        blank=True,
    )
    age_stop_smoking = models.IntegerField(
        verbose_name="If past smoker, at what age did you stop smoking?",
        help_text="in years",
        null=True,
        blank=True,
    )
    someone_else_smoke = models.CharField(
        verbose_name="Is there anyone in your home/work places who smoke cigarette, cigars, shisha and pipes",
        max_length=15,
        choices=YES_NO,
    )
    smoke_inside_house = models.CharField(
        verbose_name="How often does anyone smoke inside your house?",
        max_length=45,
        choices=SMOKE_INSIDE,
        default=NOT_APPLICABLE,
    )
    smoke_inside_house_other = edcs_models.OtherCharField()

    consume_alcohol = models.CharField(
        verbose_name="Do you consume alcohol?",
        max_length=45,
        choices=ALCOHOL_CONSUMPTION,
    )
    alcohol_consumption_frequency = models.CharField(
        verbose_name="How frequently do you consume alcohol?",
        max_length=45,
        choices=ALCOHOL_CONSUMPTION_FREQUENCY,
        default=NOT_APPLICABLE,
    )
    alcohol_consumption_frequency_other = edcs_models.OtherCharField()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Alcohol Tobacco Use"
        verbose_name_plural = "Alcohol Tobacco Use"

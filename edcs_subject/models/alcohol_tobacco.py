from django.db import models

from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models

from ..choices import (
    ALCOHOL_CONSUMPTION,
    ALCOHOL_CONSUMPTION_FREQUENCY,
    SMOKE_INSIDE,
    SMOKE_TOBACCO_PRODUCTS,
    SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
    TOBACCO_PRODUCTS,
)


class AlcoholTobaccoUse(
    edcs_models.BaseUuidModel,
):

    smoke_tobacco = models.CharField(
        verbose_name="Do you smoke tobacco products?",
        max_length=15,
        choices=SMOKE_TOBACCO_PRODUCTS,
    )

    tobacco_product = models.DateField(
        verbose_name="If currently/past smoker, which tobacco products do you/ did you smoke.",
        max_length=45,
        choices=TOBACCO_PRODUCTS,
    )

    date_start_smoking = models.DateField(
        verbose_name="Month and Year Patient started smoking tobacco products",
        null=True,
        blank=True,
    )

    smoking_frequency = models.CharField(
        verbose_name="How frequently do you smoke these products?",
        max_length=45,
        choices=SMOKE_TOBACCO_PRODUCTS_FREQUENCY,
    )

    smoking_frequency_other = edcs_models.OtherCharField()

    no_tobacco_product_smoked = models.IntegerField(
        verbose_name="On average, how many of these products do you/did you smoke?",
        max_length=15,
    )
    age_start_smoking = models.IntegerField(
        verbose_name="If past smoker, at what age did you first start smoking?",
        help_text="in years",
    )
    age_stop_smoking = models.IntegerField(
        verbose_name="If past smoker, at what age did you stop smoking?",
        help_text="in years",
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
    )

    alcohol_consumption_frequency_other = edcs_models.OtherCharField()

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Alcohol Tobacco Use"
        verbose_name_plural = "Alcohol Tobacco Use"

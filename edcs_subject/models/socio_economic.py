from django.db import models

from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import (
    COOKING,
    IRON,
    MATERIAL_BUILD_FLOOR,
    MATERIAL_BUILD_ROOFING,
    MATERIAL_BUILD_WALL,
    POWER_SOURCE,
)
from ..model_mixins import CrfModelMixin


class SocioEconomicCharacteristic(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    electricity = models.CharField(
        verbose_name="Do you have electricity in your household?",
        max_length=15,
        choices=YES_NO,
    )
    television = models.CharField(
        verbose_name="Do you have a television in your household?",
        max_length=15,
        choices=YES_NO,
    )
    radio = models.CharField(
        verbose_name="Do you have a radio in your household?",
        max_length=15,
        choices=YES_NO,
    )
    an_iron = models.CharField(
        verbose_name="Do you have an Iron in your household?",
        max_length=45,
        choices=IRON,
    )
    bank_account = models.CharField(
        verbose_name="Does anyone in your household own a bank account/mobile money/microfinance?",
        max_length=15,
        choices=YES_NO,
    )
    material_build_floor = models.CharField(
        verbose_name="Which materials were used to build the floor in your house?",
        max_length=45,
        choices=MATERIAL_BUILD_FLOOR,
    )

    material_build_floor_other = edcs_models.OtherCharField()

    material_build_walls = models.CharField(
        verbose_name="Which materials were used to build the walls of your house?",
        max_length=45,
        choices=MATERIAL_BUILD_WALL,
    )

    material_build_walls_other = edcs_models.OtherCharField()

    material_build_roof = models.CharField(
        verbose_name="Which materials were used for roofing your house?",
        max_length=45,
        choices=MATERIAL_BUILD_ROOFING,
    )

    material_build_roof_other = edcs_models.OtherCharField()

    use_in_cooking = models.CharField(
        verbose_name="What does your household use in cooking regularly? ",
        max_length=45,
        choices=COOKING,
    )

    use_in_cooking_other = edcs_models.OtherCharField()

    main_power_source = models.CharField(
        verbose_name="What is the main source of power lighting in your household?",
        max_length=15,
        choices=POWER_SOURCE,
    )

    main_power_source_other = edcs_models.OtherCharField()

    household_monthly_income = models.IntegerField(
        verbose_name="What is the average monthly combined income for the entire household ",
        help_text="(from ALL sources, including employment, selling crops, extra income etc.)? Amount in shillings",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Socio-Economic Characteristics"
        verbose_name_plural = "Socio-Economic Characteristics"

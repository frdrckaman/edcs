from django.db import models

from edcs_constants.choices import YES_NO
from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN1AP, QN2AP, QN3AP, QN5AP, QN7AP, QN28AP
from ..model_mixins import CrfModelMixin


class CookingFuel(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    main_use_cooking = models.CharField(
        verbose_name="What type of fuel does your household MAINLY use for cooking?",
        max_length=45,
        choices=QN1AP,
    )

    main_use_cooking_other = edcs_models.OtherCharField()

    main_reason_use = models.CharField(
        verbose_name="What is the MAIN reason why you use this?",
        max_length=125,
        choices=QN2AP,
    )

    cooking_done = models.CharField(
        verbose_name="Where is the cooking usually done?", max_length=45, choices=QN3AP
    )

    cooking_done_other = edcs_models.OtherCharField()

    no_cooking_household = models.IntegerField(
        verbose_name="How many times does your household typically cook in a day?",
    )

    sleep_where_cook = models.CharField(
        verbose_name="Do you sleep in the same room where you cook?",
        max_length=45,
        choices=QN5AP,
    )
    use_wood = models.CharField(
        verbose_name="Do you use wood to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_wood_per_month = models.CharField(
        verbose_name="If yes, how many times do you use wood per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_kerosene = models.CharField(
        verbose_name="Do you use kerosene to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_kerosene_per_month = models.CharField(
        verbose_name="If yes, how many times do you use kerosene per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_charcoal = models.CharField(
        verbose_name="Do you use charcoal to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_charcoal_per_month = models.CharField(
        verbose_name="If yes, how many times do you use charcoal per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_coal = models.CharField(
        verbose_name="Do you use coal/ignite to cook",
        max_length=45,
        choices=YES_NO,
    )
    use_coal_per_month = models.CharField(
        verbose_name="If yes, how many times do you use coal/ignite per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_straw = models.CharField(
        verbose_name="Do you use straw/shrubs/grass to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_straw_per_month = models.CharField(
        verbose_name="If yes, how many times do you use straw/shrubs/grass per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_electricity = models.CharField(
        verbose_name="Do you use electricity to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_electricity_per_month = models.CharField(
        verbose_name="If yes, how many times do you use electricity per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_biogas = models.CharField(
        verbose_name="Do you use biogas for cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_biogas_per_month = models.CharField(
        verbose_name="If yes, how many times do you use biogas per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_dung = models.CharField(
        verbose_name="Do you use animal dung to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_dung_per_month = models.CharField(
        verbose_name="If yes, how many times do you use animal dung per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_paper = models.CharField(
        verbose_name="Do you use paper to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_paper_per_month = models.CharField(
        verbose_name="If yes, how many times do you use paper per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_polythene = models.CharField(
        verbose_name="Do you use polythene to cook?",
        max_length=45,
        choices=YES_NO,
    )
    use_polythene_per_month = models.CharField(
        verbose_name="If yes, how many times do you use polythene per month?",
        max_length=45,
        choices=QN7AP,
        default=NOT_APPLICABLE,
    )
    use_burn_crops = models.CharField(
        verbose_name="Do you often burn crops, wood, rubbish, polythene or other materials in the open?",
        max_length=45,
        choices=YES_NO,
    )
    distance_from_neighbor = models.IntegerField(
        verbose_name="Estimate the distance from your household to your nearest neighbor in meters?",
    )
    neighbor_use_cooking = models.CharField(
        verbose_name="What is the MAIN type of fuel that most of your neighbors use?",
        max_length=45,
        choices=QN28AP,
    )

    neighbor_use_cooking_other = edcs_models.OtherCharField()

    smoke_from_neighbor = models.CharField(
        verbose_name="Does smoke from your neighbors cooking  or burnings enter your house?",
        max_length=45,
        choices=YES_NO,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Cooking Fuel"
        verbose_name_plural = "Cooking Fuel"

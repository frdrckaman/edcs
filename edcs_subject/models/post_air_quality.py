from django.db import models

from edcs_constants.choices import YES_NO
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import (
    AirMonitorProblem,
    OtherCookingFuel,
    SolidFuel,
    SolidFuelNew,
)
from edcs_model import models as edcs_models
from edcs_model.models import datetime_not_future
from edcs_utils import get_utcnow

from ..choices import COOKING_FUEL, FUEL_USED_HEATING, SMOKE_TOBACCO_HOUSE
from ..model_mixins import CrfModelMixin


class PostAirQuality(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text="Date and time of report.",
    )

    monitor_end_date = models.DateTimeField(
        verbose_name="Monitor end date",
        validators=[datetime_not_future],
    )

    air_monitor_problem = models.CharField(
        verbose_name="During the air monitoring, were there any problems with the household air monitor?",
        choices=YES_NO,
        max_length=15,
    )

    air_monitor_problem_list = models.ManyToManyField(
        AirMonitorProblem,
        verbose_name="If yes, select all that apply",
    )

    cooking_fuel_used = models.CharField(
        verbose_name="During the air monitoring: What was the primary fuel used for cooking?",
        choices=COOKING_FUEL,
        max_length=45,
    )

    cooking_fuel_used_other = edcs_models.OtherCharField()

    cooking_fuel_used_duration = models.IntegerField(
        verbose_name="For how many hours was the primary fuel used for cooking?",
        help_text="Enter as minutes Eg 1hr = 60min",
    )

    other_cooking_fuel = models.ManyToManyField(
        OtherCookingFuel,
        verbose_name="What other fuels were used for cooking?",
    )

    other_cooking_fuel_other = edcs_models.OtherCharField()

    other_cooking_fuel_duration = models.IntegerField(
        verbose_name="For how many hours were the other fuels used for cooking?",
        help_text="Enter as minutes Eg 1hr = 60min",
    )

    solid_fuel = models.ManyToManyField(
        SolidFuelNew,
        verbose_name="If you used solid fuel (charcoal, wood, coal, agriculture/crop, animal dung or shrub/grass) as "
        "primary fuel or other fuel for cooking, what type of stove did you use these fuels in?",
    )

    solid_fuel_other = edcs_models.OtherCharField()

    primary_fuel_heating = models.CharField(
        verbose_name="During the air monitoring, what was the primary fuel used for heating?",
        choices=FUEL_USED_HEATING,
        max_length=45,
    )

    primary_fuel_heating_other = edcs_models.OtherCharField()

    primary_fuel_heating_duration = models.IntegerField(
        verbose_name="For how many hours was the primary fuel used for heating?",
        help_text="Enter as minutes Eg 1hr = 60min",
    )

    smoke_inside = models.CharField(
        verbose_name="During the air monitoring, did people smoke tobacco products in this house?",
        choices=YES_NO,
        max_length=15,
    )

    smoke_inside_duration = models.CharField(
        verbose_name="If yes, how many times did people smoke tobacco products in this house?",
        choices=SMOKE_TOBACCO_HOUSE,
        max_length=45,
        default=NOT_APPLICABLE,
    )

    air_pollution_monitor_reading = models.DecimalField(
        verbose_name="Reading from air pollution assessment",
        decimal_places=4,
        max_digits=12,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Post Air Quality"
        verbose_name_plural = "Post Air Quality"

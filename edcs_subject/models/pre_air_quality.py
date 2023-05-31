from django.db import models

from edcs_constants.choices import GENDER, YES_NO
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import CookingArea, CookingDone
from edcs_model import models as edcs_models
from edcs_model.models import datetime_not_future
from edcs_utils import get_utcnow

from ..choices import COOKING_FUEL
from ..model_mixins import CrfModelMixin


class PreAirQuality(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text="Date and time of report.",
    )

    monitor_start_date = models.DateTimeField(
        verbose_name="Monitor start date",
        validators=[datetime_not_future],
    )

    selected_air_monitor = models.CharField(
        verbose_name="Has this household been selected for Personal Air Monitoring?",
        choices=YES_NO,
        max_length=15,
    )

    household_num = models.CharField(
        verbose_name="House hold number:",
        max_length=14,
        null=True,
        blank=True,
    )

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=45,
    )

    total_num_rooms = models.IntegerField(
        verbose_name="Total number of rooms in the household",
        help_text="including bedroom/sleeping areas and excluding bathroom",
    )

    total_num_windows = models.IntegerField(
        verbose_name="Total number of windows in the household"
    )

    cooking_done = models.ManyToManyField(
        CookingDone,
        verbose_name="Where is the cooking for the household done?",
    )

    cooking_area = models.ManyToManyField(
        CookingArea,
        verbose_name="If inside the house, Does the inside cooking area have any of the following?",
    )

    cooking_done_outside = models.IntegerField(
        verbose_name="If outside the house, on average how many months per year do you cook outside?",
        help_text="If less than 1 month, enter 01",
    )

    cooking_fuel = models.CharField(
        verbose_name="What is the primary fuel currently used for cooking?",
        choices=COOKING_FUEL,
        max_length=45,
    )

    cooking_fuel_other = edcs_models.OtherCharField()

    cooking_fuel_duration = models.IntegerField(
        verbose_name="For how long have you been using this primary fuel for cooking?",
        help_text="If duration is less than 1 year, please indicate “01”",
    )

    previously_used_cooking_fuel = models.CharField(
        verbose_name="Was there a previous primary fuel used for cooking?",
        choices=YES_NO,
        max_length=15,
    )

    previously_cooking_fuel = models.CharField(
        verbose_name="If yes, what was the previous primary fuel used for cooking?",
        choices=COOKING_FUEL,
        max_length=45,
        default=NOT_APPLICABLE,
    )

    previously_cooking_fuel_other = edcs_models.OtherCharField()

    previously_cooking_fuel_duration = models.IntegerField(
        verbose_name="For how long did you use the previous primary fuel for cooking? ",
        help_text="If duration is less than 1 year, please indicate “01”",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Pre Air Quality"
        verbose_name_plural = "Pre Air Quality"

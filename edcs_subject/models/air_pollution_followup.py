from django.db import models

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN49EAP, QN50EAP


class AirPollutionFollowUp(
    edcs_models.BaseUuidModel,
):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    hour_wear_device = models.IntegerField(
        verbose_name="In the past 48 hours how many hours did you wear devices?",
    )

    who_had_illness = models.CharField(
        verbose_name="What type of fuel did you use for cooking since we visited your home yesterday",
        max_length=45,
        choices=QN49EAP,
    )

    fuel_before_changing = models.CharField(
        verbose_name="What type of stove did you use for cooking since we visited your home yesterday?",
        max_length=125,
        choices=QN50EAP,
    )

    pollution_readings = models.CharField(
        verbose_name="What is the air pollution readings",
        max_length=125,
    )

    gps_coordinates = models.TextField(
        verbose_name="Record GPS coordinates of the patient’s home using the nearest physical feature on the google map",
        max_length=125,
    )

    distance_health_facility = models.IntegerField(
        verbose_name="Distance from patient’s home to the health facility",
        help_text="(in km)",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Effect of Air Pollution"
        verbose_name_plural = "Effect of Air Pollution"

from django.db import models

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin
from ..choices import QN49EAP, QN50EAP


class AirPollutionFollowUp(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    hour_wear_device = models.IntegerField(
        verbose_name="In the past 48 hours how many hours did you wear devices?",
    )

    fuel_type_used = models.CharField(
        verbose_name="What type of fuel did you use for cooking since we visited your home yesterday",
        max_length=45,
        choices=QN49EAP,
    )

    fuel_type_used_other = edcs_models.OtherCharField()

    stove_type_used = models.CharField(
        verbose_name="What type of stove did you use for cooking since we visited your home yesterday?",
        max_length=125,
        choices=QN50EAP,
    )

    stove_type_used_other = edcs_models.OtherCharField()

    pollution_readings = models.DecimalField(
        verbose_name="What is the air pollution readings",
        max_digits=6,
        decimal_places=4
    )

    gps_coordinates = models.TextField(
        verbose_name="Record GPS coordinates of the patient’s home using the nearest physical feature on the google map",
        max_length=125,
    )

    distance_health_facility = models.DecimalField(
        verbose_name="Distance from patient’s home to the health facility",
        max_digits=4,
        decimal_places=2,
        help_text="(in km)",
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Air Pollution Follow Up"
        verbose_name_plural = "Air Pollution Follow Up"

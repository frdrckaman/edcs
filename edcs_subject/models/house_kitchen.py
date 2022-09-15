from django.db import models

from edcs_constants.choices import YES_NO
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN30AP, QN31AP, QN32AP, QN34AP, QN36AP, QN39AP
from ..model_mixins import CrfModelMixin


class HouseKitchenSurrounding(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    material_floor = models.CharField(
        verbose_name="What is the main material of the floor of the dwelling?",
        max_length=45,
        choices=QN30AP,
    )

    material_roof = models.CharField(
        verbose_name="What is the main material of the roof of the dwelling?",
        max_length=45,
        choices=QN31AP,
    )

    material_interior_wall = models.CharField(
        verbose_name="What is the main material of the interior walls of the dwelling?",
        max_length=125,
        choices=QN32AP,
    )

    material_exterior_wall = models.CharField(
        verbose_name="What is the main material of the exterior walls of the dwelling?",
        max_length=15,
        choices=QN32AP,
    )

    inside_swept = models.CharField(
        verbose_name="How often is the inside of the dwelling swept?",
        max_length=125,
        choices=QN34AP,
    )
    material_kitchen_floor = models.CharField(
        verbose_name="What is the main material of the kitchen floor?",
        max_length=125,
        choices=QN30AP,
    )
    material_kitchen_roof = models.CharField(
        verbose_name="What is the main material of the kitchen roof?",
        max_length=125,
        choices=QN36AP,
    )
    material_interior_wall_kitchen = models.CharField(
        verbose_name="What is the main material of the interior walls of your kitchen?",
        max_length=125,
        choices=QN32AP,
    )
    material_exterior_wall_kitchen = models.CharField(
        verbose_name="What is the main material of the exterior walls of your kitchen?",
        max_length=125,
        choices=QN32AP,
    )
    kitchen_swept = models.CharField(
        verbose_name="How often is the inside of the kitchen swept?",
        max_length=125,
        choices=QN39AP,
    )
    no_kitchen_window = models.IntegerField(
        verbose_name="How many windows in the kitchen open to outside the house?",
    )
    no_kitchen_door = models.IntegerField(
        verbose_name="How many doors in the kitchen open to outside the house?",
    )
    kitchen_chimney = models.CharField(
        verbose_name="Does the kitchen have a chimney?", max_length=15, choices=YES_NO
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "House Kitchen Surrounding"
        verbose_name_plural = "House Kitchen Surrounding"

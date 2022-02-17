from django.db import models

from edcs_constants.choices import YES_NO
from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin
from ..choices import QN44EAP


class EffectAirPollution(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    family_member_sickness = models.CharField(
        verbose_name="Has any member of your family had any sickness that made you change the type of fuel you use?",
        max_length=45,
        choices=YES_NO,
    )

    who_had_illness = models.CharField(
        verbose_name="If yes, please state, who had the illness",
        max_length=45,
        choices=QN44EAP,
        default=NOT_APPLICABLE
    )

    fuel_before_changing = models.CharField(
        verbose_name="If you changed fuel, what fuel were you using before and which fuel did you change to?",
        max_length=125,
        blank=True,
        null=True,
    )

    variation_btn_fuel = models.CharField(
        verbose_name="Is there any seasonal variation between primary and secondary fuel used for cooking?",
        max_length=15,
        choices=YES_NO,
    )

    influence_variation_btn_fuel = models.CharField(
        verbose_name="If yes, Can you tell us how season influences your choice of fuel?",
        max_length=125,
        blank=True,
        null=True,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Effect of Air Pollution"
        verbose_name_plural = "Effect of Air Pollution"

from django.db import models

from edcs_constants.choices import YES_NO_DECLINED_TO_ANSWER
from edcs_model import models as edcs_models

from ..choices import QN65, QN72


class OccupationalHistory(
    edcs_models.BaseUuidModel,
):

    history_working_industries = models.CharField(
        verbose_name="Do you have history of working in industries?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    industries_worked_on = models.CharField(
        verbose_name="If yes, what kind of industry did you work?",
        max_length=45,
        choices=QN72,
    )

    history_working_mines = models.CharField(
        verbose_name="Do you have history of working in the mines?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    how_long_work_mine = models.CharField(
        verbose_name="If yes, for how long have worked in the mines?",
        max_length=45,
        choices=QN65,
    )

    activities_expose_to_smoke = models.TextField(
        verbose_name="Are there any activities or daily events that expose you to smoke or dust on a daily basis that we have not asked you about, if true list them",
        blank=True,
        null=True,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Occupational History"
        verbose_name_plural = "Occupational History"

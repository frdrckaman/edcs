from django.db import models

from edcs_constants.choices import YES_NO_DECLINED_TO_ANSWER_NA
from edcs_constants.constants import NOT_APPLICABLE
from edcs_lists.models import Contraceptives
from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..choices import QN60, QN61, QN62, QN64, QN65, QN66, QN70
from ..model_mixins import CrfModelMixin


class ContraceptiveUseReproductiveHistory(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    age_attain_menarche = models.CharField(
        verbose_name="At what age did you attain your menarche?",
        max_length=45,
        choices=QN60,
        default=NOT_APPLICABLE,
    )

    age_have_first_child = models.CharField(
        verbose_name="At what age did you have your first child?",
        max_length=45,
        choices=QN61,
        default=NOT_APPLICABLE,
    )

    age_have_last_child = models.CharField(
        verbose_name="At what age did you have your last child?",
        max_length=45,
        choices=QN62,
        default=NOT_APPLICABLE,
    )

    breast_feed = models.CharField(
        verbose_name="Have you ever breast fed?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER_NA,
        default=NOT_APPLICABLE,
    )

    use_contraceptives = models.CharField(
        verbose_name="Have you ever used any contraceptives?",
        max_length=45,
        choices=QN64,
        default=NOT_APPLICABLE,
    )

    contraceptives = models.ManyToManyField(
        Contraceptives,
        verbose_name="If the answer is yes, which type of contraceptives have you ever used?",
    )

    contraceptives_other = edcs_models.OtherCharField()

    how_long_use_contraceptives = models.CharField(
        verbose_name="If yes, how long have you been using the named above contraceptives?",
        max_length=45,
        choices=QN65,
        default=NOT_APPLICABLE,
    )
    when_stop_use_contraceptives = models.CharField(
        verbose_name="For those who have stopped using oral contraceptive, when did you stop?",
        max_length=45,
        choices=QN66,
        default=NOT_APPLICABLE,
    )
    post_menopausal_hormone_therapy = models.CharField(
        verbose_name="Have you ever used post-menopausal hormone therapy?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER_NA,
        default=NOT_APPLICABLE,
    )
    how_long_post_menopausal_hormone_therapy = models.CharField(
        verbose_name="If yes, how long have you been using/ have you used post-menopausal therapy?",
        max_length=45,
        choices=QN65,
        default=NOT_APPLICABLE,
    )

    how_long_stop_post_menopausal_hormone_therapy = models.CharField(
        verbose_name="For those who have stopped using post-menopausal hormone therapy, when did you "
        "stop using post-menopausal therapy?",
        max_length=45,
        choices=QN66,
        default=NOT_APPLICABLE,
    )

    age_attain_menopause = models.CharField(
        verbose_name="For menopausal women, at what age did you attain menopause?",
        max_length=45,
        choices=QN70,
        default=NOT_APPLICABLE,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Contraceptive Use Reproductive History"
        verbose_name_plural = "Contraceptive Use Reproductive History"

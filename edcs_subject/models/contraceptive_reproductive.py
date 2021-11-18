from django.db import models

from edcs_constants.choices import YES_NO_DECLINED_TO_ANSWER
from edcs_model import models as edcs_models

from ..choices import QN60, QN61, QN62, QN64, QN65, QN66, QN70


class ContraceptiveUseReproductiveHistory(
    edcs_models.BaseUuidModel,
):

    age_attain_menarche = models.CharField(
        verbose_name="At what age did you attain your menarche?",
        max_length=45,
        choices=QN60,
    )

    age_have_first_child = models.CharField(
        verbose_name="At what age did you have your first child?",
        max_length=45,
        choices=QN61,
    )

    age_have_last_child = models.CharField(
        verbose_name="At what age did you have your last child?",
        max_length=45,
        choices=QN62,
    )

    breast_feed = models.CharField(
        verbose_name="Have you ever breast fed?",
        max_length=45,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )

    use_oral_contraceptives = models.CharField(
        verbose_name="Have you ever used oral contraceptives?",
        max_length=45,
        choices=QN64,
    )
    how_long_use_oral_contraceptives = models.CharField(
        verbose_name="If yes, how long have you been using oral contraceptives?",
        max_length=45,
        choices=QN65,
    )
    when_stop_use_contraceptives = models.CharField(
        verbose_name="For those who have stopped using oral contraceptive, when did you stop?",
        max_length=45,
        choices=QN66,
    )
    post_menopausal_hormone_therapy = models.CharField(
        verbose_name="Have you ever used post-menopausal hormone therapy?",
        max_length=15,
        choices=YES_NO_DECLINED_TO_ANSWER,
    )
    how_long_post_menopausal_hormone_therapy = models.CharField(
        verbose_name="If yes, how long have you been using/ have you used post-menopausal therapy? ",
        max_length=45,
        choices=QN65,
    )

    how_long_stop_post_menopausal_hormone_therapy = models.CharField(
        verbose_name="For those who have stopped using post-menopausal hormone therapy, when did you stop using"
        " post-menopausal therapy?",
        max_length=45,
        choices=QN66,
    )

    age_attain_menopause = models.CharField(
        verbose_name="For menopausal women, at what age did you attain menopause?",
        max_length=45,
        choices=QN70,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Contraceptive Use Reproductive History"
        verbose_name_plural = "Contraceptive Use Reproductive History"

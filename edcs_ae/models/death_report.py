from edcs_crf.crf_model_mixins import CrfModelMixin
from edcs_model import models as edcs_models

from ..model_mixins import DeathReportModelMixin


class DeathReport(DeathReportModelMixin):
    class Meta(DeathReportModelMixin.Meta):
        pass

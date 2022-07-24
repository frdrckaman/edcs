from ..model_mixins import DeathReportModelMixin


class DeathReport(DeathReportModelMixin):
    class Meta(DeathReportModelMixin.Meta):
        pass

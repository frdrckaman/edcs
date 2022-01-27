from edcs_crf.crf_status_model_mixin import CrfStatusModelMixin
from edcs_crf.model_mixins import CrfModelMixin as BaseCrfModelMixin


class CrfModelMixin(CrfStatusModelMixin, BaseCrfModelMixin):
    class Meta(BaseCrfModelMixin.Meta):
        abstract = True

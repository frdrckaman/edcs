from django.contrib.sites.managers import CurrentSiteManager
from edcs_visit_schedule.managers import CrfModelManager
from edcs_model.models import HistoricalRecords
from .crf_no_manager_model_mixin import CrfNoManagerModelMixin


class CrfModelMixin(CrfNoManagerModelMixin):

    on_site = CurrentSiteManager()
    objects = CrfModelManager()
    history = HistoricalRecords(inherit=True)

    class Meta(CrfNoManagerModelMixin.Meta):
        abstract = True

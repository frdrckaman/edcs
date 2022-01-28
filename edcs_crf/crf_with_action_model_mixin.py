from django.contrib.sites.managers import CurrentSiteManager
# from edcs_action_item.models import ActionNoManagersModelMixin
from edcs_identifier.model_mixins import TrackingModelMixin
from edcs_model.models.historical_records import HistoricalRecords
from edcs_visit_schedule.managers import CrfModelManager

from .crf_model_mixins import CrfNoManagerModelMixin


class CrfWithActionModelMixin(
    CrfNoManagerModelMixin,
    # ActionNoManagersModelMixin,
    TrackingModelMixin,
):

    action_name = None
    tracking_identifier_prefix = ""

    on_site = CurrentSiteManager()
    objects = CrfModelManager()
    history = HistoricalRecords(inherit=True)

    class Meta(CrfNoManagerModelMixin.Meta):
        abstract = True

from django.conf import settings
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.db.models.deletion import PROTECT
from edcs_consent.model_mixins import RequiresConsentFieldsModelMixin
from edcs_identifier.model_mixins import TrackingModelMixin
from edcs_model.models.historical_records import HistoricalRecords
from edcs_sites.models import SiteModelMixin
from edcs_visit_schedule.managers import CrfModelManager
from edcs_visit_schedule.model_mixins import (
    VisitTrackingCrfModelMixin,
)

from .stubs import CrfModelStub


class CrfNoManagerModelMixin(
    VisitTrackingCrfModelMixin,
    RequiresConsentFieldsModelMixin,
    SiteModelMixin,
):
    """Base model for all scheduled models"""

    subject_visit = models.OneToOneField(settings.SUBJECT_VISIT_MODEL, on_delete=PROTECT)

    def natural_key(self: CrfModelStub) -> tuple:
        return self.subject_visit.natural_key()

    natural_key.dependencies = [  # type:ignore
        settings.SUBJECT_VISIT_MODEL,
        "sites.Site",
        "edc_appointment.appointment",
    ]

    class Meta:
        abstract = True
        indexes = [models.Index(fields=["subject_visit", "site", "id"])]
        default_permissions = ("add", "change", "delete", "view", "export", "import")


class CrfModelMixin(CrfNoManagerModelMixin):

    on_site = CurrentSiteManager()
    objects = CrfModelManager()
    history = HistoricalRecords(inherit=True)

    class Meta(CrfNoManagerModelMixin.Meta):
        abstract = True


class CrfWithActionModelMixin(
    CrfNoManagerModelMixin,
    TrackingModelMixin,
):

    action_name = None
    tracking_identifier_prefix = ""

    on_site = CurrentSiteManager()
    objects = CrfModelManager()
    history = HistoricalRecords(inherit=True)

    class Meta(CrfNoManagerModelMixin.Meta):
        abstract = True

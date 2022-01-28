from django.conf import settings
from django.db import models
from edcs_consent.model_mixins import RequiresConsentFieldsModelMixin
from edcs_sites.models import SiteModelMixin
from edcs_visit_schedule.model_mixins import (
    VisitTrackingCrfModelMixin,
)


class CrfNoManagerModelMixin(
    VisitTrackingCrfModelMixin,
    RequiresConsentFieldsModelMixin,
    SiteModelMixin,
):
    """Base model for all scheduled models"""

    subject_visit = models.OneToOneField(
        settings.SUBJECT_VISIT_MODEL, on_delete=models.PROTECT
    )

    def natural_key(self) -> tuple:
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

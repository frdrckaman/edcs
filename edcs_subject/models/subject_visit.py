from django.db import models
from edcs_consent.model_mixins import RequiresConsentFieldsModelMixin
from edcs_constants.constants import NOT_APPLICABLE
from edcs_model import models as edc_models
from edcs_sites.models import CurrentSiteManager as BaseCurrentSiteManager
from edcs_sites.models import SiteModelMixin

from ..choices import INFO_SOURCE, VISIT_REASON, VISIT_UNSCHEDULED_REASON


class CurrentSiteManager(BaseCurrentSiteManager):
    pass


class SubjectVisit(
    # VisitModelMixin,
    # ReferenceModelMixin,
    SiteModelMixin,
    RequiresConsentFieldsModelMixin,
    edc_models.BaseUuidModel,
):
    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    reason = models.CharField(
        verbose_name="What is the reason for this visit report?",
        max_length=25,
        choices=VISIT_REASON,
    )

    reason_unscheduled = models.CharField(
        verbose_name="If 'unscheduled', provide reason for the unscheduled visit",
        max_length=25,
        choices=VISIT_UNSCHEDULED_REASON,
        default=NOT_APPLICABLE,
    )

    clinic_services_other = edc_models.OtherCharField()

    info_source = models.CharField(
        verbose_name="What is the main source of this information?",
        max_length=25,
        choices=INFO_SOURCE,
    )

    on_site = CurrentSiteManager()

    # objects = VisitModelManager()

    history = edc_models.HistoricalRecords()

    # class Meta(VisitModelMixin.Meta, edc_models.BaseUuidModel.Meta):
    #     pass

    class Meta(edc_models.BaseUuidModel.Meta):
        pass

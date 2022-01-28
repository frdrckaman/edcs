from django.db import models
from edcs_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edcs_model import models as edcs_models
from edcs_visit_schedule.model_mixins import (
    VisitCodeFieldsModelMixin,
    VisitScheduleFieldsModelMixin,
)


class CrfStatus(
    NonUniqueSubjectIdentifierFieldMixin,
    VisitScheduleFieldsModelMixin,
    VisitCodeFieldsModelMixin,
    edcs_models.BaseUuidModel,
):
    label_lower = models.CharField(max_length=150, null=True)

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "CRF Status"
        verbose_name_plural = "CRF Status"

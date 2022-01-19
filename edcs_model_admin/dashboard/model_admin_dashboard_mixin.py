from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edcs_model_admin import (
    ModelAdminAuditFieldsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminNextUrlRedirectMixin,
    ModelAdminRedirectOnDeleteMixin,
    ModelAdminReplaceLabelTextMixin,
    TemplatesModelAdminMixin,
)
# from edcs_notification import NotificationModelAdminMixin


class ModelAdminDashboardMixin(
    TemplatesModelAdminMixin,
    # ModelAdminNextUrlRedirectMixin,
    # NotificationModelAdminMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminRevisionMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
    ModelAdminReplaceLabelTextMixin,
):
    pass

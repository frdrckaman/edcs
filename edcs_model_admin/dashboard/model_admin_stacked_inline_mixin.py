from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from edcs_model_admin import (
    ModelAdminAuditFieldsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminNextUrlRedirectMixin,
    ModelAdminRedirectOnDeleteMixin,
    TemplatesModelAdminMixin,
)
# from edcs_notification import NotificationModelAdminMixin


class ModelAdminStackedInlineMixin(
    TemplatesModelAdminMixin,
    ModelAdminNextUrlRedirectMixin,
    # NotificationModelAdminMixin,
    ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin,
    ModelAdminRevisionMixin,
    ModelAdminAuditFieldsMixin,
    ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin,
):
    pass

from edcs_fieldsets.fieldsets_modeladmin_mixin import FieldsetsModelAdminMixin
from edcs_visit_schedule.modeladmin_mixin import CrfModelAdminMixin

from .model_admin_dashboard_mixin import ModelAdminDashboardMixin


class ModelAdminCrfDashboardMixin(
    FieldsetsModelAdminMixin,
    ModelAdminDashboardMixin,
    CrfModelAdminMixin,
):

    show_save_next = True
    show_cancel = True
    show_dashboard_in_list_display_pos = 1

    def get_subject_dashboard_url_kwargs(self, obj):
        return dict(
            subject_identifier=obj.subject_visit.subject_identifier,
            appointment=str(obj.subject_visit.appointment.id),
        )

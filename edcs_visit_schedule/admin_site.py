from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_visit_schedule_admin = EdcsAdminSite(
    name="edcs_visit_schedule_admin", app_label=AppConfig.name
)

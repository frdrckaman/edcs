from edcs_model_admin.admin_site import EdcsAdminSite
from .apps import AppConfig

edcs_notification_admin = EdcsAdminSite(name="edcs_notification_admin", app_label=AppConfig.name)

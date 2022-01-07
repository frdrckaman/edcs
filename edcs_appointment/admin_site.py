from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_appointment_admin = EdcsAdminSite(name="edcs_appointment_admin", app_label=AppConfig.name)

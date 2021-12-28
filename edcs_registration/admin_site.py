from edcs_model_admin.admin_site import EdcsAdminSite
from .apps import AppConfig

edcs_registration_admin = EdcsAdminSite(name="edcs_registration_admin", app_label=AppConfig.name)

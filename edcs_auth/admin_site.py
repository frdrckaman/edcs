from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_auth_admin = EdcsAdminSite(name="edcs_auth_admin", app_label=AppConfig.name)

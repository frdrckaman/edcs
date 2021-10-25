from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_identifier_admin = EdcsAdminSite(name="edcs_identifier_admin", app_label=AppConfig.name)

from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_export_admin = EdcsAdminSite(name="edcs_export_admin", app_label=AppConfig.name)

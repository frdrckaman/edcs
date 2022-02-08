from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_lists_admin = EdcsAdminSite(name="edcs_lists_admin", app_label=AppConfig.name)

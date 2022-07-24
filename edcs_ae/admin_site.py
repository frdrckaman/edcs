from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_ae_admin = EdcsAdminSite(name="edcs_ae_admin", app_label=AppConfig.name)

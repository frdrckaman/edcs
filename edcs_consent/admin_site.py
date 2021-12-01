from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_consent_admin = EdcsAdminSite(name="edcs_consent_admin", app_label=AppConfig.name)

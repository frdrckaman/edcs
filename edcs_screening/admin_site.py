from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_screening_admin = EdcsAdminSite(name="edcs_screening_admin", app_label=AppConfig.name)

from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_subject_admin = EdcsAdminSite(name="edcs_subject_admin", app_label=AppConfig.name)

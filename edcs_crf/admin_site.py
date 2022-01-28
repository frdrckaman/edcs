from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_crf_admin = EdcsAdminSite(name="edcs_crf_admin", app_label=AppConfig.name)

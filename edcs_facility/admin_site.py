from edcs_model_admin.admin_site import EdcsAdminSite

from .apps import AppConfig

edcs_facility_admin = EdcsAdminSite(name="edcs_facility_admin", app_label=AppConfig.name)

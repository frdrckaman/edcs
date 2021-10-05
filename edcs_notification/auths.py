from edcs_auth.auth_objects import ACCOUNT_MANAGER_ROLE
from edcs_auth.site_auths import site_auths
from edcs_export.auth_objects import EXPORT

from .auth_objects import NOTIFICATION, codenames

site_auths.add_group(*codenames, name=NOTIFICATION)
site_auths.update_group("edc_notification.export_notification", name=EXPORT)
site_auths.update_role(NOTIFICATION, name=ACCOUNT_MANAGER_ROLE)

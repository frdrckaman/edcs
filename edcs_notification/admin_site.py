from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site


class EdcsAdminSite(DjangoAdminSite):
    def __init__(self, name="admin"):
        super().__init__(name)
        del self._actions["delete_selected"]

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        return context

    site_url = "/administration/"
    enable_nav_sidebar = False  # DJ 3.1


class AdminSite(EdcsAdminSite):
    site_title = "Edcs Notification"
    site_header = "Edcs Notification"
    index_title = "Edcs Notification"


edcs_notification_admin = AdminSite(name="edcs_notification_admin")

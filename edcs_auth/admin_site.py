from django.contrib import admin
from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site

admin.site.enable_nav_sidebar = False


class EdcAdminSite(DjangoAdminSite):
    def __init__(self, name="admin"):
        super().__init__(name)
        del self._actions["delete_selected"]

    def each_context(self, request):
        context = super().each_context(request)
        context.update(global_site=get_current_site(request))
        return context

    site_url = "/administration/"
    enable_nav_sidebar = False  # DJ 3.1


class AdminSite(EdcAdminSite):
    site_header = "Edcs Authentication"
    site_title = "Edcs Authentication"
    index_title = "Edcs Authentication"


edcs_auth_admin = AdminSite(name="edcs_auth_admin")

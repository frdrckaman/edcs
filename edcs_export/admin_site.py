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


class EdcsExportAdminSite(DjangoAdminSite):
    site_header = "Edcs Export"
    site_title = "Edcs Export"
    index_title = "Edcs Export Administration"
    site_url = "/"


edcs_export_admin = EdcsExportAdminSite(name="edcs_export_admin")
edcs_export_admin.disable_action("delete_selected")

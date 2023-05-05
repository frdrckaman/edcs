from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_export_admin

app_name = "edcs_export"

urlpatterns = [
    path("admin/", edcs_export_admin.urls),
    path("", RedirectView.as_view(url="/edcs_export/admin/"), name="home_url"),
]

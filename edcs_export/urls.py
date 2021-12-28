from django.urls.conf import path

from edcs_dashboard.views import HomeView
from .admin_site import edcs_export_admin


app_name = "edcs_export"

urlpatterns = [
    path("admin/", edcs_export_admin.urls),
    path("", HomeView.as_view(), name="home_url"),
]

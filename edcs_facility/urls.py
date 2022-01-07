from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_facility_admin

app_name = "edcs_facility"

urlpatterns = [
    path("admin/", edcs_facility_admin.urls),
    path("", RedirectView.as_view(url=f"admin/"), name="home_url"),
]

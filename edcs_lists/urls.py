from django.urls import path
from django.views.generic import RedirectView
from .admin_site import edcs_lists_admin

app_name = "edcs_lists"

urlpatterns = [
    path("admin/", edcs_lists_admin.urls),
    path("", RedirectView.as_view(url="/edcs_lists/admin/"), name="home_url"),
]

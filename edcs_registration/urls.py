from django.urls.conf import path
from django.views.generic.base import RedirectView
from .admin_site import edcs_registration_admin

app_name = "edcs_registration"

urlpatterns = [
    path("admin/", edcs_registration_admin.urls),
    path("", RedirectView.as_view(url="/edcs_registration/admin/"), name="home_url"),
]

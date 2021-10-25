from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_identifier_admin

app_name = "edcs_identifier"

urlpatterns = [
    path("admin/", edcs_identifier_admin.urls),
    path("", RedirectView.as_view(url="/edcs_identifier/admin/"), name="home_url"),
]

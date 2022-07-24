from django.urls.conf import path
from django.views.generic import RedirectView

from .admin_site import edcs_ae_admin

app_name = "edcs_ae"

urlpatterns = [
    path("admin/", edcs_ae_admin.urls),
    path("", RedirectView.as_view(url="/edcs_ae/admin/"), name="home_url"),
]

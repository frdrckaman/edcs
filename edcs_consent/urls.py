from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_consent_admin

app_name = "edcs_consent"

urlpatterns = [
    path("admin/", edcs_consent_admin.urls),
    path("", RedirectView.as_view(url="/edcs_consent/admin/"), name="home_url"),
]

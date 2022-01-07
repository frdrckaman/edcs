from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_appointment_admin

app_name = "edcs_appointment"

urlpatterns = [
    path("admin/", edcs_appointment_admin.urls),
    path("", RedirectView.as_view(url="/edcs_appointment/admin/"), name="home_url"),
]

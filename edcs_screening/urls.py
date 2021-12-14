from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_screening_admin

app_name = "edcs_screening"

urlpatterns = [
    path("admin/", edcs_screening_admin.urls),
    path("", RedirectView.as_view(url="/edcs_screening/admin/"), name="home_url"),
]

from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_visit_schedule_admin

app_name = "edcs_visit_schedule"

urlpatterns = [
    path("admin/", edcs_visit_schedule_admin.urls),
    path("", RedirectView.as_view(url="/edcs_visit_schedule/admin/"), name="home_url"),
]
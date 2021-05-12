from django.urls import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_notification_admin

app_name = "edcs_notification"

urlpatterns = [
    path("admin/", edcs_notification_admin.urls),
    path("", RedirectView.as_view(url="/edcs_notification/admin/"), name="home_url"),
]

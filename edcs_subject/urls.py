from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import edcs_subject_admin

app_name = "edcs_subject"

urlpatterns = [
    path("admin/", edcs_subject_admin.urls),
    path("", RedirectView.as_view(url="/edcs_subject/admin/"), name="home_url"),
]

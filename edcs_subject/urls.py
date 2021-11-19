from django.urls.conf import path
from django.views.generic import RedirectView

app_name = "edcs_subject"

urlpatterns = [
    path("", RedirectView.as_view(url="/edcs_subject_admin/"), name="home_url"),
]

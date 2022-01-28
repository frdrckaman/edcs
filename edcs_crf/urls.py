from django.urls import path
from django.views.generic import RedirectView

app_name = "edcs_crf"

urlpatterns = [
    path("", RedirectView.as_view(url=f"/{app_name}/admin/"), name="home_url"),
]


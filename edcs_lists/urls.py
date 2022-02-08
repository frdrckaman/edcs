from django.urls import path
from django.views.generic import RedirectView

app_name = "edcs_lists"

urlpatterns = [
    path("", RedirectView.as_view(url="/edcs_lists_admin/"), name="home_url"),
]

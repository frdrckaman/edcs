from django.urls.conf import path
from edcs_device.views import HomeView


app_name = "edcs_device"

urlpatterns = [path("", HomeView.as_view(), name="home_url")]

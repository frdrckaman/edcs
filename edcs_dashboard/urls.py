from django.urls import path
from edcs_dashboard.views import HomeView

app_name = "edcs_dashboard"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]

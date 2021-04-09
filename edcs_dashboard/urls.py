from django.urls import path

from edcs_dashboard.views import DashboardView

app_name = "edcs_dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name="home"),
]

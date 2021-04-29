from django.urls import path
from .views import edcs_vac083Home
from edcs_dashboard.views import DashboardView
from edcs_vac083.views import DemographicView


app_name = 'edcs_vac083'

urlpatterns = [
    path('', edcs_vac083Home, name="vac083"),
    # path("demographic/", DemographicView, name="demographic"),
    path("demographic", DemographicView.as_view(), name="demographic"),
]

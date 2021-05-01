from django.urls import path
from edcs_vac083.views import DemographicView, DemographicCreate, edcs_vac083_home, edcs_vac083_visits
from django.contrib import admin

app_name = 'edcs_vac083'

urlpatterns = [
    path("DemographicView", DemographicView.as_view(), name="DemographicView"),
    path('DemographicCreate/', DemographicCreate, name='DemographicCreate'),
    path('edcs_vac083_home/', edcs_vac083_home.as_view(), name='edcs_vac083_home'),
    path('edcs_vac083_visits/', edcs_vac083_visits.as_view(), name='edcs_vac083_visits'),
    path('admin/', admin.site.urls),
]

from django.urls import path
from edcs_vac083.views import DemographicView, DemographicCreate
from django.contrib import admin


app_name = 'edcs_vac083'

urlpatterns = [
    path("DemographicView", DemographicView, name="DemographicView"),
    path('DemographicCreate/', DemographicCreate, name='DemographicCreate'),
    path('admin/', admin.site.urls),
]

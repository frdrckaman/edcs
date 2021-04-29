from django.urls import path
from django.contrib import admin
from edcs_rab002.views import DemographicCreate


urlpatterns = [
    path('DemographicCreate/', DemographicCreate, name='DemographicCreate'),
    path('admin/', admin.site.urls),
]
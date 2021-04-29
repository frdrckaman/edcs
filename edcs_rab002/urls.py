from django.urls import path
from django.contrib import admin
from edcs_rab002.views import DemographicCreate, DemographicEdit


urlpatterns = [
    path('DemographicCreate/', DemographicCreate, name='DemographicCreate'),
    path('DemographicEdit/<int:pk>', DemographicEdit, name='DemographicEdit'),
    path('admin/', admin.site.urls),
]
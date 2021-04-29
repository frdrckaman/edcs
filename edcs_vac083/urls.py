from django.urls import path
from . import views


app_name = 'edcs_vac083'

urlpatterns = [
    path('', views.edcs_vac083_home, name='edcs_vac083_home'),
]

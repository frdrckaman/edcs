from django.urls import path
from edcs_vac083.views import edcs_vac083Home


app_name = 'edcs_vac083'

urlpatterns = [
    path('', edcs_vac083Home, name="vac083"),
]

from django.urls import path
from edcs_vac083_home.vi


app_name = 'edcs_vac083'

urlpatterns = [
    # path('', views.edcs_vac083_home, name='edcs_vac083_home'),
    path('vac083/home/', edcs_vac083_home.as_view(template_name='edcs_vac083/edcs_vac083_home.html'),
         name='edcs_vac083_home'),
]

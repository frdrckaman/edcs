from django.urls.conf import path
from django.views.generic.base import RedirectView

from .admin_site import edcs_screening_admin
from .views import ScreeningDashboardView

app_name = "edcs_screening"

urlpatterns = [
    path("admin/", edcs_screening_admin.urls),
    path('screening/', ScreeningDashboardView.as_view(), name="screening_dashboard"),
    path("", RedirectView.as_view(url="/edcs_screening/admin/"), name="home_url"),
]

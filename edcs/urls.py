from django.contrib import admin
from django.urls import path, include

from edcs_dashboard.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('edcs_auth.urls')),
    path("dashboard/", include("edcs_dashboard.urls")),
    path("home/", DashboardView.as_view(), name="home_url"),
    path("maqz/", include("edcs_vac083.urls")),
]

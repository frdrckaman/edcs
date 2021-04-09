from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('edcs_auth.urls')),
    path("dashboard/", include("edcs_dashboard.urls")),
]

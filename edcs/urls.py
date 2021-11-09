from django.contrib import admin
from django.urls import path, include

from edcs_dashboard.views import AdministrationView
from edcs_notification.admin_site import edcs_notification_admin
from edcs_export.admin_site import edcs_export_admin
from edcs_identifier.admin_site import edcs_identifier_admin
from edcs_screening.admin_site import edcs_screening_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', edcs_export_admin.urls),
    path('admin/', edcs_notification_admin.urls),
    path('admin/', edcs_identifier_admin.urls),
    path('admin/', edcs_screening_admin.urls),
    path("", include('edcs_auth.urls')),
    path("dashboard/", include("edcs_dashboard.urls")),
    path("edcs_device/", include("edcs_device.urls")),
    path("edcs_notification/", include("edcs_notification.urls")),
    path("edcs_export/", include("edcs_export.urls")),
    path("edcs_identifier/", include("edcs_identifier.urls")),
    path("edcs_screening/", include("edcs_screening.urls")),
    # path("home/", DashboardView.as_view(), name="home_url"),
    path("administration/", AdministrationView.as_view(), name="administration_url"),
]

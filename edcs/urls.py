from django.contrib import admin
from django.urls import include, path

from edcs_dashboard.views import AdministrationView
from edcs_export.admin_site import edcs_export_admin
from edcs_identifier.admin_site import edcs_identifier_admin
from edcs_notification.admin_site import edcs_notification_admin
from edcs_screening.admin_site import edcs_screening_admin
from edcs_subject.admin_site import edcs_subject_admin
from edcs_consent.admin_site import edcs_consent_admin
from edcs_registration.admin import edcs_registration_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin/", edcs_export_admin.urls),
    path("admin/", edcs_notification_admin.urls),
    path("admin/", edcs_identifier_admin.urls),
    path("admin/", edcs_screening_admin.urls),
    path("admin/", edcs_subject_admin.urls),
    path("admin/", edcs_consent_admin.urls),
    path("admin/", edcs_registration_admin.urls),
    path("", include("edcs_auth.urls")),
    path("dashboard/", include("edcs_dashboard.urls")),
    path("edcs_device/", include("edcs_device.urls")),
    path("edcs_notification/", include("edcs_notification.urls")),
    path("edcs_export/", include("edcs_export.urls")),
    path("edcs_identifier/", include("edcs_identifier.urls")),
    path("edcs_screening/", include("edcs_screening.urls")),
    path("edcs_subject/", include("edcs_subject.urls")),
    path("edcs_consent/", include("edcs_consent.urls")),
    path("edcs_registration/", include("edcs_registration.urls")),
    # path("home/", DashboardView.as_view(), name="home_url"),
    path("administration/", AdministrationView.as_view(), name="administration_url"),
]

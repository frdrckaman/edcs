from django.contrib import admin
from django.urls import path

from edcs_dashboard.views import (
    CrfListView,
    DownloadListView,
    EnrollDashboardView,
    EnrollListView,
    HomeView,
    ScreeningDashboardView,
    download_data,
    download_dict,
)

app_name = "edcs_dashboard"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("enroll-list/", EnrollListView.as_view(), name="enroll-list"),
    path("download-list/", DownloadListView.as_view(), name="download-list"),
    path("enroll-list/<page>", EnrollListView.as_view(), name="enroll-list"),
    path(
        "enroll-dashboard/<subject>/", EnrollDashboardView.as_view(), name="enroll-dashboard"
    ),
    path("crf-list/<subject>/<appointment>", CrfListView.as_view(), name="crf-list"),
    path("screening/", ScreeningDashboardView.as_view(), name="screening_dashboard"),
    path("screening/<page>", ScreeningDashboardView.as_view(), name="screening_dashboard"),
    path("download-data/", download_data, name="download-data"),
    path("download-dict/", download_dict, name="download-dict"),
    path("", HomeView.as_view(), name="home"),
]

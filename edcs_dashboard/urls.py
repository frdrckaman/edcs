from django.urls import path
from django.contrib import admin
from edcs_dashboard.views import HomeView, EnrollListView, EnrollDashboardView, CrfListView

app_name = "edcs_dashboard"

urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('enroll-list/', EnrollListView.as_view(), name="enroll-list"),
    path('enroll-dashboard/', EnrollDashboardView.as_view(), name='enroll-dashboard'),
    path('crf-list/', CrfListView.as_view(), name='crf-list'),
]

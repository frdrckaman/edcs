from django.urls import path
from django.contrib import admin
from edcs_dashboard.views import HomeView, EnrollListView, EnrollDashboardView, CrfListView, ScreeningDashboardView

app_name = "edcs_dashboard"

urlpatterns = [path("admin/", admin.site.urls)]

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('enroll-list/', EnrollListView.as_view(), name="enroll-list"),
    path('enroll-dashboard/<subject>/', EnrollDashboardView.as_view(), name='enroll-dashboard'),
    path('crf-list/<subject>/<appointment>', CrfListView.as_view(), name='crf-list'),
    path('screening/', ScreeningDashboardView.as_view(), name='screening_dashboard')
]

from django.urls import path
from django.contrib import admin
from edcs_dashboard.views import HomeView

app_name = "edcs_dashboard"

urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]

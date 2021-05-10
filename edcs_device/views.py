from django.apps import apps as django_apps
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edcs_dashboard.view_mixins import EdcsViewMixin

from .view_mixins import EdcDeviceViewMixin


class HomeView(EdcsViewMixin, EdcDeviceViewMixin, TemplateView):

    template_name = f"edcs_device/bootstrap{settings.EDCS_BOOTSTRAP}/home.html"
    navbar_name = "edcs_device"
    navbar_selected_item = "device"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_config = django_apps.get_app_config("edcs_device")
        project_name = context.get("project_name")
        context.update({"project_name": f"{project_name}: {app_config.verbose_name}"})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

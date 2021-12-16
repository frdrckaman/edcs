from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edcs_dashboard.views.screening_list.screening_listboard import ListboardView


class ScreeningDashboardView(ListboardView, TemplateView):

    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/screening.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            edcs_packages=["not available"],
            third_party_packages=["not available"],
            installed_apps=settings.INSTALLED_APPS,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

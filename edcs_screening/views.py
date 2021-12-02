from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from .models import SubjectScreening


class ScreeningDashboardView(TemplateView):
    template_name = f"edcs_screening/bootstrap{settings.EDCS_BOOTSTRAP}/screening.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            edc_packages=["not available"],
            third_party_packages=["not available"],
            installed_apps=settings.INSTALLED_APPS,
            screening_url=SubjectScreening().admin_url_name
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

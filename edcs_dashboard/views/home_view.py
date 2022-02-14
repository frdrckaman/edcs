from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.models import Site
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_profile = Site.objects.get_current()
        context.update(
            installed_apps=settings.INSTALLED_APPS,
            s_id=site_profile.id
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


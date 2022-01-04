from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


class EnrollListView(TemplateView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/enroll_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            # edc_packages=["not available"],
            third_party_packages=["not available"],
            installed_apps=settings.INSTALLED_APPS,
        )
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


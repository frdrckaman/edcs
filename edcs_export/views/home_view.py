from django.conf import settings
from django.views.generic import TemplateView
from edcs_dashboard.view_mixins import EdcsViewMixin


class HomeView(EdcsViewMixin, TemplateView):

    template_name = f"edcs_export/bootstrap{settings.EDCS_BOOTSTRAP}/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

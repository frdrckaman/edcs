from django.conf import settings
from django.views.generic.base import TemplateView
from edcs_dashboard.view_mixins import EdcsViewMixin

from edcs_protocol import Protocol


class HomeView(EdcsViewMixin, TemplateView):
    template_name = f"edcs_protocol/bootstrap{settings.EDCS_BOOTSTRAP}/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        protocol = Protocol()
        context.update(
            {
                "protocol": protocol.protocol,
                "protocol_number": protocol.protocol_number,
                "protocol_name": protocol.protocol_name,
                "protocol_title": protocol.protocol_title,
                "study_open_datetime": protocol.study_open_datetime,
                "study_close_datetime": protocol.study_close_datetime,
            }
        )
        return context

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .screening_list.screening_listboard import ScreeningListBoardView


class ScreeningDashboardView(ScreeningListBoardView):

    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/screening.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

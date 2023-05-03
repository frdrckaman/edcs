from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edcs_dashboard.views.subject_list import SubjectListBoardView


class DownloadListView(SubjectListBoardView):
    template_name = f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/download_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

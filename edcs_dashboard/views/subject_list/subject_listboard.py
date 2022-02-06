from django.core.paginator import Paginator
from django.views.generic import TemplateView

from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_registration.models import RegisteredSubject


# TODO create a ListView
class SubjectListBoardView(ListboardView, TemplateView):
    listboard_url = "subject_listboard_url"
    listboard_model = "edcs_registration.registeredsubject"
    model_consent = "edcs_registration.registeredsubject"
    ordering = "-created"
    listboard_dashboard = "edcs_dashboard:enroll-dashboard"

    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(RegisteredSubject, 10)

        page_number = None
        page_obj = paginator
        context.update(
            object_list=self.object_list_subject(RegisteredSubject),
            page_obj=page_obj,
        )
        return context

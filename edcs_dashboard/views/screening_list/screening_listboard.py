from edcs_dashboard.views.dashboard_list import ListboardView
from edcs_screening.models import SubjectScreening


class ScreeningListBoardView(ListboardView):
    listboard_url = "screening_listboard_url"
    listboard_model = "edcs_screening.subjectscreening"
    ordering = "-report_datetime"
    listboard_dashboard = "edcs_dashboard:screening_dashboard"

    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_screening_add_url=self.get_subject_screening_add_url(),
            object_list=self.object_list(SubjectScreening),
        )
        return context

    def get_subject_screening_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

    @property
    def screening_data(self):
        return SubjectScreening.objects.all().order_by(self.ordering).values()

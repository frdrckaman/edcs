from edcs_dashboard.views.subject_list import SubjectDashboardView


class CrfListBoardView(SubjectDashboardView):
    listboard_url = "subject_listboard_url"
    model_consent = "edcs_registration.registeredsubject"
    ordering = "-created"
    listboard_dashboard = "edcs_dashboard:crf-list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

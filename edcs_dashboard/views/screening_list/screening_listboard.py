from edcs_dashboard.views.dashboard_list.listboard_view import ListboardView


class ListboardView(ListboardView):
    listboard_url = "screening_listboard_url"
    listboard_model = "edcs_screening.subjectscreening"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            subject_screening_add_url=self.get_subject_screening_add_url(),
        )
        return context

    def get_subject_screening_add_url(self):
        return self.listboard_model_cls().get_absolute_url()

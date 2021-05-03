from django.views.generic import TemplateView
from edcs_dashboard.view_mixins import AdministrationViewMixin, EdcsViewMixin


class AdministrationView(
    EdcsViewMixin, AdministrationViewMixin, TemplateView
):

    navbar_selected_item = "administration"
    # navbar_name = "default"  # settings.APP_NAME

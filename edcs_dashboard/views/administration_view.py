from django.views.generic import TemplateView
from ..view_mixins import AdministrationViewMixin, EdcsViewMixin


class AdministrationView(EdcsViewMixin, AdministrationViewMixin, TemplateView):

    navbar_selected_item = "administration"

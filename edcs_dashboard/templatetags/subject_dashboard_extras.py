from pprint import pprint
from bs4 import BeautifulSoup
from django import template
from django.conf import settings
from ..views.dashboard_list import Struct

register = template.Library()

# TODO MODIFY THIS TEMPLATE
@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/screening_button.html",
    takes_context=True,
)
def screening_button(context, result):
    title = "Edit subject's screening form"
    obj = Struct(**result)
    return dict(
        # perms=context["perms"],
        screening_identifier=obj.screening_identifier,
        href=result.get('href'),
        title=title,
    )
import datetime
from pprint import pprint

from django import template
from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/template-theme-settings.html",
    takes_context=True,
)
def theme_settings(context):
    title = None
    return dict(
        title=title,
    )

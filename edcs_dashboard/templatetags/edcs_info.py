import pdb

from django import template
from django.conf import settings
from edcs_protocol import Protocol
from django_revision.revision import site_revision

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/info.html",
    takes_context=True,
)
def EdcsInfo(context):
    protocol = Protocol()
    return {
        "DEBUG": settings.DEBUG,
        "copyright": protocol.copyright,
        "disclaimer": protocol.disclaimer,
        "institution": protocol.institution,
        "license": protocol.license,
        "project_name": protocol.project_name,
        "revision": site_revision.tag,
    }


@register.simple_tag
def edcs_name():
    return settings.EDCS_NAME

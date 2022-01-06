from pprint import pprint

from bs4 import BeautifulSoup
from django import template
from django.conf import settings
from edcs_constants.constants import TBD
from ..views.dashboard_list import Struct

from edcs_screening.eligibility import (
    calculate_eligible_final,
    eligibility_display_label,
)

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/screening_button.html",
)
def screening_button(result):
    title = "Edit subject's screening form"
    obj = Struct(**result)
    return dict(
        screening_identifier=obj.screening_identifier,
        href=result.get('href'),
        title=title,
    )


# TODO convert result into object instead of the list
@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/eligibility_button.html"
)
def eligibility_button(result):
    comment = []
    '''convert dict to object'''
    obj = Struct(**result)
    tooltip = None
    if not obj.eligible and obj.reasons_ineligible:
        comment = obj.reasons_ineligible.split("|")
        comment = list(set(comment))
        # comment.sort()
    soup = BeautifulSoup(eligibility_display_label(obj), features="html.parser")
    return dict(
        eligible=obj.eligible,
        eligible_final=calculate_eligible_final(obj),
        display_label=soup.get_text(),
        comment=comment,
        tooltip=tooltip,
        TBD=TBD,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/buttons/add_consent_button.html",
)
def add_consent_button(result):
    title = ["Consent subject to participate."]
    obj = Struct(**result)
    return dict(
        eligible=obj.eligible,
        screening_identifier=obj.screening_identifier,
        subject_consent_add_url=obj.subject_consent_add_url,
        consented=obj.consented,
        href='',
        consent_version='',
        title=" ".join(title),
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/dashboard_button.html"
)
def dashboard_button(result):
    title = "Go to Subject's Dashboard"
    obj = Struct(**result)
    return dict(
        consented=obj.consented,
        subject_dashboard_url=obj.subject_dashboard_url,
        subject_identifier=None,
        title=title,
    )

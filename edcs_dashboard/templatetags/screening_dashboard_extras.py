from pprint import pprint

from bs4 import BeautifulSoup
from django import template
from django.conf import settings
from edcs_constants.constants import NO, TBD, YES
from edcs_dashboard.url_names import url_names

from edcs_screening.eligibility import (
    calculate_eligible_final,
    eligibility_display_label,
)

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/screening_button.html",
    takes_context=True,
)
def screening_button(context, result):
    title = "Edit subject's screening form"
    return dict(
        # perms=context["perms"],
        screening_identifier=result.get('screening_identifier'),
        href=result.get('href'),
        title=title,
    )


# TODO convert result into object instead of the list
@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/eligibility_button.html"
)
def eligibility_button(subject_screening_model_wrapper):
    comment = []
    obj = subject_screening_model_wrapper.object
    tooltip = None
    if not obj.eligible and obj.reasons_ineligible:
        comment = obj.reasons_ineligible.split("|")
        comment = list(set(comment))
        comment.sort()
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
    takes_context=True,
)
def add_consent_button(context, model_wrapper):
    title = ["Consent subject to participate."]
    consent_version = model_wrapper.consent.version
    return dict(
        perms=context["perms"],
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.consent.href,
        consent_version=consent_version,
        title=" ".join(title),
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/buttons/refusal_button.html",
    takes_context=True,
)
def refusal_button(context, model_wrapper):
    title = ["Capture subject's primary reason for not joining."]
    return dict(
        perms=context["perms"],
        screening_identifier=model_wrapper.object.screening_identifier,
        href=model_wrapper.refusal.href,
        title=" ".join(title),
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/dashboard_button.html"
)
def dashboard_button(model_wrapper):
    subject_dashboard_url = url_names.get("subject_dashboard_url")
    return dict(
        subject_dashboard_url=subject_dashboard_url,
        subject_identifier=model_wrapper.subject_identifier,
    )

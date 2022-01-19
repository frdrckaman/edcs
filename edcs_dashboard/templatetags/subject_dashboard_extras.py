import datetime
from pprint import pprint

from django import template
from django.conf import settings

from edcs_appointment.models import Appointment
from edcs_utils import age

register = template.Library()


# TODO MODIFY THIS THAT YOU DONT HAVE TO PASS DATA TO IT (result) get all info from context
@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/side-info-panel.html",
)
def side_info_panel(result):
    return dict(
        subject_identifier=result.subject_identifier,
        gender=result.gender,
        dob=result.dob.strftime("%Y-%m-%d"),
        age=age(result.dob, datetime.datetime.now()).years,
        initials=result.initials,
        identity=result.identity,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/consent-panel.html",
)
def consent_panel(result):
    title = "Subject's Consent Form"
    return dict(
        href=result,
        title=title,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/start_visit_button.html",
    takes_context=True,
)
def start_visit(context, visit):
    listboard_dashboard = "edcs_dashboard:enroll-dashboard"
    title = "Start Subject's Visit"

    appointment = Appointment.objects.get(
        subject_identifier=context.get("subject"), visit_code=visit
    )
    nxt = listboard_dashboard + "&subject=" + context.get("subject")

    return dict(
        href=next_url(appointment.admin_url(appointment.id), nxt),
        title=title,
    )


def next_url(url, nxt):
    return "?next=".join([url, nxt])

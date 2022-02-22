import datetime

from django import template
from django.conf import settings
from django.urls import reverse

from edcs_appointment.constants import NEW_APPT, IN_PROGRESS_APPT, OPEN_TIMEPOINT
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
    takes_context=True,
)
def consent_panel(context):
    title = "Subject's Consent Form"
    return dict(
        href=context.get('consent_url'),
        consent_date=context.get('consent_date'),
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
        status=appointment.appt_status
    )


def next_url(url, nxt):
    return "?next=".join([url, nxt])


# TODO make all tags that query Appointment use this function
def appointment(subject_identifier, visit_code):
    return Appointment.objects.get(
        subject_identifier=subject_identifier, visit_code=visit_code
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/start_button.html",
    takes_context=True,
)
def start_button(context, appt):
    listboard_dashboard = "edcs_dashboard:crf-list"
    title = "Start Appointment"
    appointment = Appointment.objects.get(subject_identifier=context.get("subject"), visit_code=appt.visit_code)

    nxt = listboard_dashboard + "&subject=" + context.get("subject") + "&appointment=" + str(appointment.id)

    return dict(
        href=next_url(context.get("subject_visit"), nxt),
        title=title,
        appt_status=appointment.appt_status
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/forms_button.html",
    takes_context=True,
)
def form_button(context, visit_code):
    listboard_dashboard = "edcs_dashboard:crf-list"
    title = "Subject Form's"
    appt_status = False
    appt = appointment(context.get("subject"), visit_code)

    if appt.appt_status == IN_PROGRESS_APPT and appt.timepoint_status == OPEN_TIMEPOINT:
        appt_status = True

    return dict(
        title=title,
        appt_status=appt_status,
        href=reverse(listboard_dashboard, args=[context.get("subject"), appt.id])
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/done_button.html",
    takes_context=True,
)
def done_button(context):
    title = "Done"
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/appointment_button.html",
    takes_context=True,
)
def appointment_button(context, visit_code):
    title = "Subject's Appointment"
    disabled = None
    if appointment(context.get("subject"), visit_code).appt_status == NEW_APPT:
        disabled = "disabled"
    return dict(
        title=title,
        disabled=disabled,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"paginator/paginator_row.html",
    takes_context=True,
)
def pagination(context):
    page_obj = context.get("page_obj")
    num_pages = "a" * page_obj.paginator.num_pages if page_obj else 1
    show_pagination = True if page_obj.paginator.num_pages > 12 else False

    return dict(
        page_obj=page_obj,
        pages=page_obj.paginator.num_pages,
        num_pages=num_pages,
        show_pagination=show_pagination,
    )


def page_numbers(page, numpages):
    page_numbers_ = None
    if page and numpages:
        min_n = page - 5
        min_n = 1 if min_n <= 0 else min_n
        max_n = min_n + 9
        max_n = numpages if max_n >= numpages else max_n
        page_numbers_ = [x for x in range(min_n, max_n + 1)]
    return page_numbers_ or []


@register.simple_tag(takes_context=True)
def expected_date(context, visit_code):
    return appointment(context.get("subject"), visit_code).appt_datetime


@register.simple_tag(takes_context=True)
def modified_date(context, visit_code):
    return appointment(context.get("subject"), visit_code).modified

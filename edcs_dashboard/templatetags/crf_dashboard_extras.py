from pprint import pprint

from django import template
from django.conf import settings
from django.urls import reverse

from edcs_subject.models import SubjectVisit

register = template.Library()


def next_url(url, nxt):
    return "?next=".join([url, nxt])


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"buttons/add_edit_crf_button.html",
    takes_context=True,
)
def add_edit_crf(context, url):
    listboard_dashboard = "edcs_dashboard:crf-list"
    subject_identifier = context.get("subject")
    appointment = context.get("appointment")

    subject_visit = SubjectVisit.objects.get(appointment_id=appointment)
    nxt = listboard_dashboard + "&subject=" + subject_identifier + "&appointment=" + appointment + "subject_visit=" + str(subject_visit.id)

    pprint(next_url(reverse(url), nxt))

    title = "Add"
    return dict(
        title=title,
        href=next_url(reverse(url), nxt)
    )

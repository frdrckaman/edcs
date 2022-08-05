from django import template
from django.conf import settings
from django.urls import reverse

from edcs_subject.models import SubjectVisit

register = template.Library()


def next_url(url, nxt):
    return "?next=".join([url, nxt])


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"buttons/add_edit_crf_button.html",
    takes_context=True,
)
def add_edit_crf(context, obj):
    listboard_dashboard = "edcs_dashboard:crf-list"
    subject_identifier = context.get("subject")
    appointment = context.get("appointment")
    text = "Add "
    icon = "glyphicon-plus"
    btn = "btn-warning"
    title = text + obj.verbose_name

    subject_visit = SubjectVisit.objects.get(appointment_id=appointment)
    subject_visit_data = obj.get_subject_visit(subject_visit.id)

    nxt = (
        listboard_dashboard
        + "&subject="
        + subject_identifier
        + "&appointment="
        + appointment
        + "&subject_visit="
        + str(subject_visit.id)
    )
    href = next_url(reverse(obj.model_cls().admin_url_name), nxt)

    if subject_visit_data:
        text = "Change "
        icon = "glyphicon-pencil"
        btn = "btn-success"
        title = text + obj.verbose_name
        href = next_url(obj.model_cls().admin_url(subject_visit_data.id), nxt)

    return dict(title=title, text=text, icon=icon, btn=btn, href=href)

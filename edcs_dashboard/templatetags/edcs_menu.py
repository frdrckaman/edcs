from django import template
from django.conf import settings

from edcs_registration.models import RegisteredSubject
from edcs_screening.models import SubjectScreening

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


@register.simple_tag
def subject_enrolled():
    return RegisteredSubject.objects.all().count()


@register.simple_tag
def subject_screened():
    return SubjectScreening.objects.all().count()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/main-menu.html",
    takes_context=True,
)
def main_menu(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/bottom-summary.html",
    takes_context=True,
)
def bottom_summary(context):

    return dict(
        enrolled=enrolled(context),
        screened=screened(context),
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/top-button-icons.html",
    takes_context=True,
)
def top_button_icon(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/news-update.html",
    takes_context=True,
)
def news_updates(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/summary-menu.html",
    takes_context=True,
)
def summary_menu(context):
    return dict(
        screened=screened(context),
        enrolled=enrolled(context),
    )


def site_(context):
    site_id = context.get('s_id') if not context.get('site_profile') else context.get('site_profile').site_id
    return site_id


def enrolled(context):
    return RegisteredSubject.objects.filter(site_id=site_(context)).count()


def screened(context):
    return SubjectScreening.objects.filter(site_id=site_(context)).count()

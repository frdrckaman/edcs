from pprint import pprint

from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from edcs_registration.models import RegisteredSubject
from edcs_screening.models import SubjectScreening

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/"
    f"menu/template-theme-settings.html",
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
    site_id = (
        context.get("s_id")
        if not context.get("site_profile")
        else context.get("site_profile").site_id
    )
    return site_id


def enrolled(context):
    return RegisteredSubject.objects.filter(site_id=site_(context)).count()


def screened(context):
    return SubjectScreening.objects.filter(site_id=site_(context)).count()


@register.simple_tag
def site_name():
    current_site = Site.objects.get_current()
    return current_site.name


@register.simple_tag
def server():
    return server_state()


@register.simple_tag
def color_code():
    if settings.EDCS_SITES_LIVE_DOMAIN:
        return "#0ad00e"
    else:
        return "firebrick"


def server_state():
    if settings.DEBUG:
        state = "DEBUG"
    elif settings.EDCS_SITES_UAT_DOMAIN:
        state = "UAT"
    elif settings.EDCS_SITES_LIVE_DOMAIN:
        state = "LIVE"
    else:
        state = None

    return state


@register.simple_tag
def live_server():
    if settings.EDCS_SITES_LIVE_DOMAIN:
        return True
    elif settings.DEBUG or settings.EDCS_SITES_UAT_DOMAIN:
        return False

import datetime
from pprint import pprint
from bs4 import BeautifulSoup
from django import template
from django.conf import settings
from edcs_utils import get_dob, age

register = template.Library()


# TODO MODIFY THIS THAT YOU DONT HAVE TO PASS DATA TO IT (result) get all info from context
@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/side-info-panel.html",
)
def side_info_panel(result):
    pprint(age(result.dob, datetime.datetime.now()).years)
    return dict(
        subject_identifier=result.subject_identifier,
        gender=result.gender,
        dob=result.dob.strftime("%Y-%m-%d"),
        age=age(result.dob, datetime.datetime.now()).years,
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

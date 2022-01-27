from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag(
    f"edcs_dashboard/bootstrap{settings.EDCS_BOOTSTRAP}/" f"menu/add_edit_crf_button.html",
    takes_context=True,
)
def add_edit_crf(context):
    title = "Add"
    return dict(
        title=title,
    )


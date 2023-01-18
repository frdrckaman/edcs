import sys

from django.apps.config import AppConfig as DjangoAppConfig
from django.core.management.color import color_style

from .site_visit_schedules import site_visit_schedules

style = color_style()


def populate_visit_schedule(sender=None, **kwargs):
    from .models import VisitSchedule

    sys.stdout.write(style.MIGRATE_HEADING("Populating visit schedule:\n"))
    VisitSchedule.objects.update(active=False)
    site_visit_schedules.to_model(VisitSchedule)
    sys.stdout.write("Done.\n")
    sys.stdout.flush()


class AppConfig(DjangoAppConfig):
    name = "edcs_visit_schedule"
    verbose_name = "Edcs Visit Schedules"
    validate_models = True
    include_in_administration_section = True

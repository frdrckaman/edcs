from django.core.management.base import BaseCommand
from edcs_visit_schedule.models import VisitSchedule
from edcs_visit_schedule.visit_schedule.study_schedule import visits


class AlreadyRegisteredVisit(Exception):
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        for visit in visits:
            schedule = VisitSchedule(**visit)
            schedule.save()

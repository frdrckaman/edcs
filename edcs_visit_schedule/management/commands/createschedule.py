from pprint import pprint

from django.core.management.base import BaseCommand, CommandError
from edcs_visit_schedule.models import VisitSchedule
from edcs_visit_schedule.visit_schedule.study_schedule import visits


class AlreadyRegisteredVisit(Exception):
    pass


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'
    # pprint(visits)

    def handle(self, *args, **options):
        # create instance of model and save to the database
        for visit in visits:
            schedule = VisitSchedule(**visit)
            schedule.save()

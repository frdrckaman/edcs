from ..site_visit_schedules import site_visit_schedules
from ..visit_schedule import VisitSchedule
from .schedule import schedule_enrolment, schedule_followup

VISIT_SCHEDULE = "visit_schedule"

visit_schedule = VisitSchedule(
    name=VISIT_SCHEDULE,
    verbose_name="EDCS",
    death_report_model="edcs_ae.deathreport",
    previous_visit_schedule=None,
)

visit_schedule.add_schedule(schedule_enrolment)
visit_schedule.add_schedule(schedule_followup)

site_visit_schedules.register(visit_schedule)

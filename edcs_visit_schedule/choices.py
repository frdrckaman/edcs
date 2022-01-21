from edcs_constants.constants import OTHER, NOT_APPLICABLE
from .constants import DAYS, HOURS, MONTHS, OFF_SCHEDULE, ON_SCHEDULE, WEEKS, YEARS

SCHEDULE_STATUS = ((ON_SCHEDULE, "On schedule"), (OFF_SCHEDULE, "Off schedule"))

VISIT_INTERVAL_UNITS = (
    (HOURS, "Hours"),
    (DAYS, "Days"),
    (WEEKS, "Weeks"),
    (MONTHS, "Months"),
    (YEARS, "Years"),
)

VISIT_REASON_UNSCHEDULED = (
    ("patient_unwell_outpatient", "Patient unwell (outpatient)"),
    ("patient_hospitalised", "Patient hospitalised"),
    (OTHER, "Other"),
    (NOT_APPLICABLE, "Not applicable"),
)

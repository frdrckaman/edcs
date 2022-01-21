from .constants import (
    CANCELLED_APPT,
    COMPLETE_APPT,
    IN_PROGRESS_APPT,
    INCOMPLETE_APPT,
    NEW_APPT,
    SCHEDULED_APPT,
    UNSCHEDULED_APPT, OPEN_TIMEPOINT, CLOSED_TIMEPOINT, NEW_TIMEPOINT, START_TIMEPOINT, INCOMPLETE_TIMEPOINT,
    START_APPT,
)

# choices for the model, see also `get_appt_reason_choices`
DEFAULT_APPT_REASON_CHOICES = (
    (SCHEDULED_APPT, "Routine / Scheduled"),
    (UNSCHEDULED_APPT, "Unscheduled"),
)


APPT_STATUS = (
    (START_APPT, "Start"),
    (IN_PROGRESS_APPT, "In Progress"),
    (INCOMPLETE_APPT, "Incomplete"),
    (COMPLETE_APPT, "Done"),
    (CANCELLED_APPT, "Cancelled"),
)

APPT_TYPE = (
    ("clinic", "In clinic"),
    ("home", "At home"),
    ("hospital", "In hospital"),
    ("telephone", "By telephone"),
)

INFO_PROVIDER = (("subject", "Subject"), ("other", "Other person"))

TIMEPOINT_STATUS = (
    (NEW_TIMEPOINT, "New"),
    (START_TIMEPOINT, "Start"),
    (OPEN_TIMEPOINT, "Open"),
    (INCOMPLETE_TIMEPOINT, "Incomplete"),
    (CLOSED_TIMEPOINT, "Closed"),
)

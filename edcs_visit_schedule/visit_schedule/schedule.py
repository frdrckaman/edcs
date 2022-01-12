from dateutil.relativedelta import relativedelta
from ..schedule import Schedule
from ..visit import Visit as BaseVisit
from ..constants import DAY1, MONTH6, MONTH12

from ..constants import SCHEDULE_ENROLMENT, SCHEDULE_FOLLOWUP
from .crfs import enrollment_crf
# from .crfs import crfs_prn as default_crfs_prn
# from .crfs import crfs_unscheduled as default_crfs_unscheduled
# from .requisitions import requisitions_6m, requisitions_12m, requisitions_d1

default_requisitions = None


class Visit(BaseVisit):
    def __init__(
        self,
        crfs_unscheduled=None,
        requisitions_unscheduled=None,
        crfs_prn=None,
        crfs_missed=None,
        requisitions_prn=None,
        allow_unscheduled=None,
        **kwargs
    ):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn ,
            requisitions_prn=requisitions_prn,  # or default_requisitions_prn,
            crfs_missed=crfs_missed,
            **kwargs,
        )


# schedule for new participants
schedule_enrolment = Schedule(
    name=SCHEDULE_ENROLMENT,
    verbose_name="Day 1 to Month 12",
    # onschedule_model="inte_prn.onschedulehiv",
    # offschedule_model="inte_prn.offschedulehiv",
    consent_model="edcs_consent.subjectconsent",
    appointment_model="edcs_appointment.appointment",
    # loss_to_followup_model="inte_prn.losstofollowup",
)

schedule_followup = Schedule(
    name=SCHEDULE_FOLLOWUP,
    verbose_name="Day 1 to Month 12",
    # onschedule_model="inte_prn.onschedulencd",
    # offschedule_model="inte_prn.offschedulencd",
    consent_model="edcs_consent.subjectconsent",
    appointment_model="edcs_appointment.appointment",
    # loss_to_followup_model="inte_prn.losstofollowup",
)

visit00 = Visit(
    code=DAY1,
    title="Day 1",
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    crfs=enrollment_crf,
    facility_name="5-day-clinic",
)


schedule_enrolment.add_visit(visit=visit00)
# schedule_hiv.add_visit(visit=visit06)
# schedule_hiv.add_visit(visit=visit12)
#
# schedule_ncd.add_visit(visit=visit00)
# schedule_ncd.add_visit(visit=visit06)
# schedule_ncd.add_visit(visit=visit12)

from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from edcs import settings
from edcs_appointment.models import Appointment
from edcs_screening.models import SubjectScreening
from edcs_visit_schedule.models import VisitSchedule

from .subject_consent import SubjectConsent


@receiver(
    post_save,
    weak=False,
    sender=SubjectConsent,
    dispatch_uid="subject_consent_on_post_save",
)
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    global timepoint_datetime
    if not raw:
        if not created:
            pass
        else:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier
            )

            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(
                update_fields=["subject_identifier", "consented"]
            )

            schedules = VisitSchedule.objects.all()

            for schedule in schedules:
                if schedule.timepoint == 0:
                    timepoint_datetime = datetime.now() + relativedelta(
                        months=+int(settings.EDCS_APPOINTMENT_INTERVAL)
                    )
                else:
                    timepoint_datetime = timepoint_datetime + relativedelta(
                        months=+int(settings.EDCS_APPOINTMENT_INTERVAL)
                    )

                visit_schedule = {
                    "subject_identifier": instance.subject_identifier,
                    "visit_schedule_name": schedule.visit_schedule_name,
                    "schedule_name": schedule.schedule_name,
                    "visit_code": schedule.visit_code,
                    "timepoint": schedule.timepoint,
                    "timepoint_datetime": timepoint_datetime,
                    "appt_datetime": timepoint_datetime,
                }

                appointment = Appointment(**visit_schedule)
                appointment.save()


@receiver(
    post_delete,
    weak=False,
    sender=SubjectConsent,
    dispatch_uid="subject_consent_on_post_delete",
)
def subject_consent_on_post_delete(sender, instance, using, **kwargs):
    """Updates/Resets subject screening."""

    # update subject screening
    subject_screening = SubjectScreening.objects.get(
        screening_identifier=instance.screening_identifier
    )
    subject_screening.consented = False
    subject_screening.subject_identifier = subject_screening.subject_screening_as_pk
    subject_screening.save()

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from edcs_subject.models import SubjectVisit
from .appointment import Appointment
from ..constants import START_APPT, OPEN_TIMEPOINT, IN_PROGRESS_APPT


@receiver(
    post_save,
    weak=False,
    sender=SubjectVisit,
    dispatch_uid="subject_visit_on_post_save",
)
def subject_visit_on_post_save(sender, instance, raw, created, **kwargs):
    appointment = Appointment.objects.get(id=instance.appointment.id)
    if appointment.appt_status == START_APPT:
        appointment.appt_status = IN_PROGRESS_APPT
        appointment.timepoint_status = OPEN_TIMEPOINT
        appointment.save_base(update_fields=["appt_status", "timepoint_status"])


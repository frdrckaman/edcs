from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from edcs_subject.models import SubjectVisit
from .appointment import Appointment


@receiver(
    post_save,
    weak=False,
    sender=SubjectVisit,
    dispatch_uid="subject_visit_on_post_save",
)
def subject_visit_on_post_save(sender, instance, raw, created, **kwargs):
    appointment = Appointment.objects.get(id=instance.appointment.id)
    if appointment.appt_status == 'start':
        appointment.appt_status = 'open'
        appointment.save_base(update_fields=["appt_status"])


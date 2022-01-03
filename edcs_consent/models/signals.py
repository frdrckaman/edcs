from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from edcs_screening.models import SubjectScreening
from .subject_consent import SubjectConsent


@receiver(
    post_save,
    weak=False,
    sender=SubjectConsent,
    dispatch_uid="subject_consent_on_post_save",
)
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this consented subject, if
    it does not exist.
    """
    if not raw:
        if not created:
            pass
        else:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier
            )

            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(update_fields=["subject_identifier", "consented"])


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

from django.contrib import admin
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from edcs_consent.modeladmin_mixins import ModelAdminConsentMixin
from edc_identifier import SubjectIdentifierError, is_subject_identifier_or_raise
from edcs_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
# from edcs_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from edcs_screening.models import SubjectScreening

from .admin_site import edcs_consent_admin
from .models import SubjectConsent


@admin.register(SubjectConsent, site=edcs_consent_admin)
class SubjectConsentAdmin(
    ModelAdminConsentMixin, SimpleHistoryAdmin
):
    # form = SubjectConsentForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "subject_identifier",
                    "screening_identifier",
                    "clinic_type",
                    "first_name",
                    "last_name",
                    "initials",
                    "gender",
                    "language",
                    "is_literate",
                    "witness_name",
                    "consent_datetime",
                    "dob",
                    "is_dob_estimated",
                    "identity",
                    "identity_type",
                    "confirm_identity",
                    "is_incarcerated",
                )
            },
        ),
        (
            "Review Questions",
            {
                "fields": (
                    "consent_reviewed",
                    "study_questions",
                    "assessment_score",
                    "consent_signature",
                    "consent_copy",
                ),
                "description": "The following questions are directed to the interviewer.",
            },
        ),
        audit_fieldset_tuple,
    )

    search_fields = ("subject_identifier", "screening_identifier", "identity")

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "clinic_type": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "consent_signature": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "identity_type": admin.VERTICAL,
        "is_incarcerated": admin.VERTICAL,
        "is_literate": admin.VERTICAL,
        "language": admin.VERTICAL,
        "study_questions": admin.VERTICAL,
    }

    # def delete_view(self, request, object_id, extra_context=None):
    #     """Prevent deletion if SubjectVisit objects exist."""
    #     extra_context = extra_context or {}
    #     obj = SubjectConsent.objects.get(id=object_id)
    #     try:
    #         protected = [SubjectVisit.objects.get(subject_identifier=obj.subject_identifier)]
    #     except ObjectDoesNotExist:
    #         protected = None
    #     except MultipleObjectsReturned:
    #         protected = SubjectVisit.objects.filter(subject_identifier=obj.subject_identifier)
    #     extra_context.update({"protected": protected})
    #     return super().delete_view(request, object_id, extra_context)

    def get_next_options(self, request=None, **kwargs):
        """Returns the key/value pairs from the "next" querystring
        as a dictionary.
        """
        next_options = super().get_next_options(request=request, **kwargs)
        try:
            is_subject_identifier_or_raise(next_options["subject_identifier"])
        except SubjectIdentifierError:
            next_options["subject_identifier"] = SubjectScreening.objects.get(
                subject_identifier_as_pk=next_options["subject_identifier"]
            ).subject_identifier
        except KeyError:
            pass
        return next_options

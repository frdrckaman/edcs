from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse

from edcs_consent.modeladmin_mixins import ModelAdminConsentMixin
from edcs_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edcs_model_admin.model_admin_form_auto_number_mixin import (
    ModelAdminFormAutoNumberMixin,
)

from ..admin_site import edcs_consent_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent


@admin.register(SubjectConsent, site=edcs_consent_admin)
class SubjectConsentAdmin(
    ModelAdminConsentMixin, ModelAdminFormAutoNumberMixin, SimpleHistoryAdmin
):
    form = SubjectConsentForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "subject_identifier",
                    "screening_identifier",
                    "clinic_type",
                    "patient_category",
                    "first_name",
                    "last_name",
                    "initials",
                    "nationality",
                    "nationality_other",
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
        "clinic_type": admin.VERTICAL,
        "patient_category": admin.VERTICAL,
        "nationality": admin.VERTICAL,
        "assessment_score": admin.VERTICAL,
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

    # TODO generate next url that will direct to patient dashboard
    def response_post_save_add(self, request, obj):
        nxt = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(nxt)

    def response_post_save_change(self, request, obj):
        if request.GET.get("subject"):
            nxt = reverse(request.GET.get("next"), args=[request.GET.get("subject")])
        else:
            nxt = request.GET.get("next", None)
        self.clear_message(request)
        return redirect(nxt)

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True

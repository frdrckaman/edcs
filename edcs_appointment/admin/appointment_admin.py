from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_audit_fields import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.dashboard import ModelAdminDashboardMixin
from edcs_visit_schedule.fieldsets import (
    visit_schedule_fields,
    visit_schedule_fieldset_tuple
)

from ..admin_site import edcs_appointment_admin
from ..forms import AppointmentForm
from ..models import Appointment


@admin.register(Appointment, site=edcs_appointment_admin)
class AppointmentAdmin(ModelAdminDashboardMixin, SimpleHistoryAdmin):

    show_cancel = True
    # form = AppointmentForm
    # resource_class = AppointmentResource
    # actions = [appointment_mark_as_done, appointment_mark_as_new]
    date_hierarchy = "appt_datetime"
    list_display = (
        "subject_identifier",
        "__str__",
        "dashboard",
        "appt_datetime",
        "appt_type",
        "appt_status",
        "schedule_name",
    )
    list_filter = ("visit_code", "appt_datetime", "appt_type", "appt_status")

    additional_instructions = mark_safe(
        "To start or continue to edit FORMS for this subject, change the "
        'appointment status below to "In Progress" and click SAVE. <BR>'
        "<i>Note: You may only edit one appointment at a time. "
        "Before you move to another appointment, change the appointment "
        'status below to "Incomplete or "Done".</i>'
    )

    fieldsets = (
        [
            None,
            (
                {
                    "fields": (
                        "subject_identifier",
                        "appt_datetime",
                        "appt_type",
                        "appt_status",
                        "appt_reason",
                        "comment",
                    )
                }
            ),
        ],
        [
            "Timepoint",
            (
                {
                    "classes": ("collapse",),
                    "fields": (
                        "timepoint",
                        "timepoint_datetime",
                        "visit_code_sequence",
                        "facility_name",
                    ),
                }
            ),
        ],
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "appt_type": admin.VERTICAL,
        "appt_status": admin.VERTICAL,
        "appt_reason": admin.VERTICAL,
    }

    search_fields = ("subject_identifier",)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj=obj)
        return (
            list(readonly_fields)
            + list(visit_schedule_fields)
            + [
                "subject_identifier",
                "timepoint",
                "timepoint_datetime",
                "visit_code_sequence",
                "facility_name",
            ]
        )

    def response_post_save_change(self, request, obj):
        next = request.GET.get('next', None)
        args = request.GET.get('subject', None)
        self.clear_message(request)
        return redirect(self.next(next, args))

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True

    def next(self, next, args):
        return reverse(next, args=[args])

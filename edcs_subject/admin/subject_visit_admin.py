from django.contrib import admin, messages
from django.shortcuts import redirect
from django.urls import reverse

from edcs_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edcs_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edcs_model_admin.dashboard import ModelAdminDashboardMixin
from ..forms import SubjectVisitForm

from ..modeladmin_mixins import VisitModelAdminMixin
from ..admin_site import edcs_subject_admin
from ..models import SubjectVisit


class ModelAdminMixin(ModelAdminDashboardMixin):
    pass


@admin.register(SubjectVisit, site=edcs_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, SimpleHistoryAdmin):
    show_dashboard_in_list_display_pos = 2

    form = SubjectVisitForm

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "appointment",
                    "report_datetime",
                    "reason",
                    "info_source",
                    "info_source_other",
                    "comments",
                ]
            },
        ),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple,
    )

    radio_fields = {
        "reason": admin.VERTICAL,
        "info_source": admin.VERTICAL,
    }

    def response_post_save_add(self, request, obj):
        next = request.GET.get('next', None)
        subject = request.GET.get('subject', None)
        appointment = request.GET.get('appointment', None)
        self.clear_message(request)
        return redirect(self.next(next, subject, appointment))

    def response_post_save_change(self, request, obj):
        next = request.GET.get('next', None)
        subject = request.GET.get('subject', None)
        appointment = request.GET.get('appointment', None)
        self.clear_message(request)
        return redirect(self.next(next, subject, appointment))

    def clear_message(self, request):
        storage = messages.get_messages(request)
        for msg in storage:
            pass
        storage.used = True

    def next(self, next, subject, appointment):
        return reverse(next, args=[subject, appointment])

from django.contrib import admin
from edcs_model_admin import SimpleHistoryAdmin, audit_fieldset_tuple
from edcs_visit_schedule.fieldsets import visit_schedule_fieldset_tuple
from edcs_model_admin.dashboard import ModelAdminDashboardMixin

from ..modeladmin_mixins import VisitModelAdminMixin
from ..admin_site import edcs_subject_admin
# from ..forms import SubjectVisitForm
from ..models import SubjectVisit


class ModelAdminMixin(ModelAdminDashboardMixin):
    pass


@admin.register(SubjectVisit, site=edcs_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, SimpleHistoryAdmin):
    show_dashboard_in_list_display_pos = 2

    # form = SubjectVisitForm

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "appointment",
                    "report_datetime",
                    "reason",
                    # "reason_unscheduled",
                    # "reason_unscheduled_other",
                    "clinic_services",
                    "clinic_services_other",
                    "health_services",
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
        "reason_unscheduled": admin.VERTICAL,
        "info_source": admin.VERTICAL,
    }

    filter_horizontal = [
        "clinic_services",
        "health_services",
    ]

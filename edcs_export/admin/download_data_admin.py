from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_export_admin
from ..models import DataDownload


@admin.register(DataDownload, site=edcs_export_admin)
class DataDownloadAdmin(SimpleHistoryAdmin):

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "data_type",
                )
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "data_type",
        "created",
    )

    list_filter = (
        "username",
        "first_name",
        "last_name",
        "email",
        "data_type",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "data_type",
    )

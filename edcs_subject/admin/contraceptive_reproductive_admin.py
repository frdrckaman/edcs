from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple

from edcs_crf.admin import crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..forms import ContraceptiveUseReproductiveHistoryForm
from ..models import ContraceptiveUseReproductiveHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(ContraceptiveUseReproductiveHistory, site=edcs_subject_admin)
class ContraceptiveUseReproductiveHistoryAdmin(CrfModelAdminMixin, SimpleHistoryAdmin):

    form = ContraceptiveUseReproductiveHistoryForm

    fieldsets = (
        (None, {"fields": ("subject_visit", "report_datetime")}),
        (
            "CONTRACEPTIVE USE AND REPRODUCTIVE HISTORY",
            {
                "fields": (
                    "age_attain_menarche",
                    "age_have_first_child",
                    "age_have_last_child",
                    "breast_feed",
                    "use_contraceptives",
                    "contraceptives",
                    "contraceptives_other",
                    "how_long_use_contraceptives",
                    "when_stop_use_contraceptives",
                    "post_menopausal_hormone_therapy",
                    "how_long_post_menopausal_hormone_therapy",
                    "how_long_stop_post_menopausal_hormone_therapy",
                    "age_attain_menopause",
                ),
            },
        ),
        crf_status_fieldset_tuple,
        audit_fieldset_tuple,
    )

    list_display = (
        "report_datetime",
        "age_attain_menarche",
        "age_have_last_child",
        "breast_feed",
        "use_contraceptives",
        "how_long_use_contraceptives",
        "age_attain_menopause",
        "created",
    )

    list_filter = (
        "report_datetime",
        "age_attain_menarche",
        "age_have_last_child",
        "breast_feed",
        "use_contraceptives",
        "how_long_use_contraceptives",
        "age_attain_menopause",
    )

    search_fields = ("report_datetime",)

    filter_horizontal = [
        "contraceptives",
    ]

    radio_fields = {
        "age_attain_menarche": admin.VERTICAL,
        "age_have_first_child": admin.VERTICAL,
        "age_have_last_child": admin.VERTICAL,
        "breast_feed": admin.VERTICAL,
        "use_contraceptives": admin.VERTICAL,
        "how_long_use_contraceptives": admin.VERTICAL,
        "when_stop_use_contraceptives": admin.VERTICAL,
        "post_menopausal_hormone_therapy": admin.VERTICAL,
        "how_long_post_menopausal_hormone_therapy": admin.VERTICAL,
        "how_long_stop_post_menopausal_hormone_therapy": admin.VERTICAL,
        "age_attain_menopause": admin.VERTICAL,
        "crf_status": admin.VERTICAL,
    }

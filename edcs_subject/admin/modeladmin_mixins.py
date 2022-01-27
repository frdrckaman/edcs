# from edcs_crf.admin import CrfStatusModelAdminMixin, crf_status_fieldset_tuple
from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.dashboard import (
    ModelAdminCrfDashboardMixin,
    ModelAdminSubjectDashboardMixin,
)


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(ModelAdminCrfDashboardMixin):
    pass


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):
    pass

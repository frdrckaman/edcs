from edcs_crf.admin import CrfStatusModelAdminMixin
from edcs_model_admin import SimpleHistoryAdmin
from edcs_model_admin.dashboard import (
    ModelAdminCrfDashboardMixin,
    ModelAdminSubjectDashboardMixin,
)
from ..modeladmin_mixins import SubjectAdminMethodsMixin


class ModelAdminMixin(ModelAdminSubjectDashboardMixin):
    pass


class CrfModelAdminMixin(SubjectAdminMethodsMixin, CrfStatusModelAdminMixin, ModelAdminCrfDashboardMixin):
    pass


class CrfModelAdmin(ModelAdminCrfDashboardMixin, SimpleHistoryAdmin):
    pass

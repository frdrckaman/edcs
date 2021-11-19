from django.contrib import admin
from django_audit_fields.admin import audit_fieldset_tuple

from edcs_model_admin import SimpleHistoryAdmin

from ..admin_site import edcs_subject_admin
from ..models import ClinicalReview
# from ..forms import ClinicalReviewForm
# from ..models import ClinicalReview
# from .fieldsets import treatment_pay_methods_fieldset_tuple
# from .modeladmin_mixins import CrfModelAdminMixin

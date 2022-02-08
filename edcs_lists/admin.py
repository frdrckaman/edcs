from django.contrib import admin
from edcs_list_data.admin import ListModelAdminMixin

from .admin_site import edcs_lists_admin
from .models import CovidSymptoms


@admin.register(CovidSymptoms, site=edcs_lists_admin)
class CovidSymptomsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


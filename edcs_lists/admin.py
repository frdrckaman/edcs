from django.contrib import admin
from edcs_list_data.admin import ListModelAdminMixin

from .admin_site import edcs_lists_admin
from .models import CovidSymptoms, FamilyMembers


@admin.register(CovidSymptoms, site=edcs_lists_admin)
class CovidSymptomsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(FamilyMembers, site=edcs_lists_admin)
class FamilyMembersAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass

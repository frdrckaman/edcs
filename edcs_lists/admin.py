from django.contrib import admin

from edcs_list_data.admin import ListModelAdminMixin

from .admin_site import edcs_lists_admin
from .models import (
    Contraceptives,
    CovidSymptoms,
    CovidVaccine,
    FamilyMembers,
    HIVSubtype,
    LungCancerSymptoms,
    SmokingTobaccoProducts,
    SomaticMutations,
    TobaccoProducts,
)


@admin.register(CovidSymptoms, site=edcs_lists_admin)
class CovidSymptomsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(FamilyMembers, site=edcs_lists_admin)
class FamilyMembersAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(LungCancerSymptoms, site=edcs_lists_admin)
class LungCancerSymptomsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(SmokingTobaccoProducts, site=edcs_lists_admin)
class SmokingTobaccoProductsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(TobaccoProducts, site=edcs_lists_admin)
class TobaccoProductsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Contraceptives, site=edcs_lists_admin)
class ContraceptivesAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(CovidVaccine, site=edcs_lists_admin)
class CovidVaccineAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(HIVSubtype, site=edcs_lists_admin)
class HIVSubtypeAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass


@admin.register(SomaticMutations, site=edcs_lists_admin)
class SomaticMutationsAdmin(ListModelAdminMixin, admin.ModelAdmin):
    pass

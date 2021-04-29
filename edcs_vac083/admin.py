from django.contrib import admin
from . models import Demographic


class DemographicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                      {'fields': ['subject_initials', 'subject_id']}),
        ('VISIT IDENTIFICATION',    {'fields': ['visit_date', 'visit_code']}),
        ('DEMOGRAPHIC INFORMATION', {'fields': ['gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
                                                'literate', 'education', 'address', 'coordinator_initials',
                                                'coordinator_time', 'reviewer_initials', 'reviewer_time']}),
    ]


admin.site.register(Demographic, DemographicAdmin)
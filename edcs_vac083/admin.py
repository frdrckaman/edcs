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

    list_display = ('subject_id', 'visit_date', 'subject_initials', 'gender')
    list_filter = ['subject_id']
    search_fields = ['subject_id']


admin.site.site_header = "ELECTRONIC DATA CAPTURE SYSTEM(VAC083)"
admin.site.site_title = "Data entry Area"
admin.site.index_title = "Welcome to the VAC083"


admin.site.register(Demographic, DemographicAdmin)
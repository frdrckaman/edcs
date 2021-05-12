from django.contrib import admin
from . models import Demographic, Book, Author, Publisher, ExclusionCriteria, ScreeningTwo


class DemographicAdmin(admin.ModelAdmin):
    class Media:
        js = ('https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
              'js/condition_logic.js',)

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


admin.site.site_header = "ELECTRONIC DATA CAPTURE SYSTEM (VAC083)"
admin.site.site_title = "Data entry Area"
admin.site.index_title = "Welcome to the VAC083"


admin.site.register(Demographic, DemographicAdmin)

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(ExclusionCriteria)


class ScreeningTwoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                                 {'fields': ['subject_initials', 'subject_id']}),
        ('VISIT IDENTIFICATION',               {'fields': ['visitOccur', 'visit_code', 'visit_date',
                                                           'reason', 'site_decision',
                                                           'reason_other', 'results',
                                                           'health',
                                                           'medication']}),

        ('Sample collection checklist',         {'fields': ['sample', 'sampleNumber']}),

        ('Additional or Repeat tests',          {'fields': ['additional', 'additional_test', 'additional_test_other']}),


        ('Screening Visit 2 Conclusion',         {'fields': ['procedures', 'procedures_no', 'procedures_no_other']}),

        ('Referral for treatment',               {'fields': ['referral', 'referral_yes']}),


        ('Bed Net Provision',                    {'fields': ['bednet']}),

        (None,                                   {'fields': ['coordinator_initials', 'coordinator_time',
                                                             'reviewer_initials', 'reviewer_time']}),

    ]

    list_display = ('subject_id', 'visit_date', 'subject_initials')
    list_filter = ['subject_id']
    search_fields = ['subject_id']


admin.site.register(ScreeningTwo, ScreeningTwoAdmin)



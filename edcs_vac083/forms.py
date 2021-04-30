from edcs_vac083.models import Demographic
from django.forms import ModelForm


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = ['subject_initials', 'subject_id', 'visit_date', 'visit_code',
                  'gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
                  'literate', 'education', 'address', 'coordinator_initials',
                  'coordinator_time', 'reviewer_initials', 'reviewer_time']



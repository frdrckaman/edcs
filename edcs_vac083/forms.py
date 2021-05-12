from edcs_vac083.models import Demographic, ExclusionCriteria, ScreeningTwo
from django.forms import ModelForm
from django import forms


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = ['subject_initials', 'subject_id', 'visit_date', 'visit_code',
                  'gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
                  'literate', 'education', 'address', 'coordinator_initials',
                  'coordinator_time', 'reviewer_initials', 'reviewer_time']


class ExclusionCriteriaForm(ModelForm):
    class Meta:
        model = ExclusionCriteria
        fields = '__all__'


class ScreeningTwoForm(ModelForm):
    class Meta:
        model = ScreeningTwo
        fields = '__all__'


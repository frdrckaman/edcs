from edcs_vac083.models import Demographic
from django.forms import ModelForm
from django import forms


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = ['subject_initials', 'subject_id', 'visit_date', 'visit_code',
                  'gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
                  'literate', 'education', 'address', 'coordinator_initials',
                  'coordinator_time', 'reviewer_initials', 'reviewer_time']

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

# Create a form to add Demographic
# form = DemographicForm()

# # Create a form to add Demographic
# demographic = DemographicForm.objects.get(pk=1)
# form = DemographicForm(instance=demographic)
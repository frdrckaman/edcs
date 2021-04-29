from edcs_vac083.models import Demographic
from django.forms import ModelForm


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = '__all__'
        # exclude = ['months']

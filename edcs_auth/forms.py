from django import forms
from django.contrib.auth.forms import UserChangeForm as BaseForm

from .models import UserProfile


class UserChangeForm(BaseForm):
    def clean(self):
        cleaned_data = super().clean()
        if not self.cleaned_data.get("first_name"):
            raise forms.ValidationError({"first_name": "Required"})
        if not self.cleaned_data.get("last_name"):
            raise forms.ValidationError({"last_name": "Required"})
        if not self.cleaned_data.get("email"):
            raise forms.ValidationError({"email": "Required"})
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data

    class Meta:
        model = UserProfile
        fields = "__all__"

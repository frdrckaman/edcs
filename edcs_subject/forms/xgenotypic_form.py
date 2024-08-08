from django import forms

from ..models import Genotypic


class GenotypicForm(forms.ModelForm):
    class Meta:
        model = Genotypic
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            subject_identifier = (
                kwargs.get("initial")["subject"] if kwargs.get("initial") else None
            )
            self.fields["subject_identifier"].initial = subject_identifier

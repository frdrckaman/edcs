import re

from django import forms
from django.urls.base import reverse
from django.utils.safestring import mark_safe
from edcs_constants.constants import UUID_PATTERN
from edcs_dashboard.url_names import url_names


class AlreadyConsentedFormMixin:
    def clean(self: forms.ModelForm) -> dict:
        cleaned_data = super().clean()  # type:ignore
        r = re.compile(UUID_PATTERN)
        if (
            self.instance.id
            and self.instance.subject_identifier
            and not r.match(self.instance.subject_identifier)
        ):
            # TODO url to point to enrolled patient dashboard (replace edcs_dashboard:screening_dashboard)
            url_name = "edcs_dashboard:screening_dashboard"
            url = reverse(
                url_name,
                # TODO url kwargs
                # kwargs={"subject_identifier": self.instance.subject_identifier},
            )
            msg = mark_safe(
                "Not allowed. Subject has already consented. "
                f'See subject <A href="{url}">{self.instance.subject_identifier}</A>'
            )
            raise forms.ValidationError(msg)
        return cleaned_data

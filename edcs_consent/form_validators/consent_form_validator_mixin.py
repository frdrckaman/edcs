from django import forms
from django.apps import apps as django_apps
from django.conf import settings
from edcs_form_validators import FormValidator

from edcs_consent import site_consents
from edcs_consent.site_consents import SiteConsentError


class ConsentFormValidatorMixin(FormValidator):

    """Validator mixin for forms that require consent.

    Call `get_consent_for_period_or_raise` in clean()."""

    consent_model = settings.SUBJECT_CONSENT_MODEL

    def get_consent_for_period_or_raise(self, report_datetime):
        default_consent_group = django_apps.get_app_config("edcs_consent").default_consent_group
        try:
            consent_object = site_consents.get_consent_for_period(
                model=self.consent_model,
                report_datetime=report_datetime,
                consent_group=default_consent_group,
            )
        except SiteConsentError as e:
            raise forms.ValidationError(e)
        return consent_object

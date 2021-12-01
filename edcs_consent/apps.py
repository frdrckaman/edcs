from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "edcs_consent"
    verbose_name = "Edcs Consent"
    include_in_administration_section = True

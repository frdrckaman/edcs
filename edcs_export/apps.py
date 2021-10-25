from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_export'
    verbose_name = 'Edcs Export'
    include_in_administration_section = True

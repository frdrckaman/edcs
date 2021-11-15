from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_screening'
    verbose_name = "Edcs Screening"
    include_in_administration_section = True

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_reportable'
    verbose_name = 'Edcs Reportable'

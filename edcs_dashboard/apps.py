from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_dashboard'
    include_in_administration_section = False

from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_protocol'
    verbose_name = 'Edcs Protocol'
    include_in_administration_section = True

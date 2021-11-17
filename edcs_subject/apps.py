from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'edcs_subject'
    verbose_name = 'Edcs Subject'
    include_in_administration_section = True

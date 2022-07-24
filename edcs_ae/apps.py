from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "edcs_ae"
    verbose_name = "Edcs Adverse Events"
    include_in_administration_section = True

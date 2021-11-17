from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "edcs_crf"
    verbose_name = "Edcs CRF"

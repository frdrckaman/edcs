from django.apps.config import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "edcs_visit_schedule"
    verbose_name = "Edcs Visit Schedules"
    validate_models = True
    include_in_administration_section = True

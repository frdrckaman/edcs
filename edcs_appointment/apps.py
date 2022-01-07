from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    _holidays: dict = {}
    name = "edcs_appointment"
    verbose_name = "Edcs Appointments"
    has_exportable_data = True
    include_in_administration_section = True

import sys
from datetime import datetime

from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.apps import apps as django_apps
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = "edcs_registration"
    verbose_name = "Edcs Registration"
    app_label = "edcs_registration"
    has_exportable_data = True
    include_in_administration_section = True

    def ready(self):
        sys.stdout.write(f"Loading {self.verbose_name} ...\n")
        sys.stdout.write(f"  * using {self.app_label}.registeredsubject\n")
        sys.stdout.write(f" Done loading {self.verbose_name}.\n")

    @property
    def model(self):
        return django_apps.get_model(self.app_label, "registeredsubject")


if "edcs_registration" in settings.APP_NAME:

    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig

    # class EdcsProtocolAppConfig(BaseEdcProtocolAppConfig):
    #     protocol = settings.EDCS_PROTOCOL
    #     protocol_name = settings.EDCS_PROTOCOL_PROJECT_NAME
    #     protocol_number = settings.EDCS_PROTOCOL_NUMBER
    #     protocol_title = settings.EDCS_PROTOCOL_TITLE
    #     site_code = "40"
    #     site_name = "mmrc"
    #     study_open_datetime = datetime(2016, 12, 31, 0, 0, 0, tzinfo=gettz("UTC"))
    #     study_close_datetime = datetime(2019, 12, 31, 23, 59, 59, tzinfo=gettz("UTC"))

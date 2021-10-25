import sys
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings


class AppConfig(DjangoAppConfig):
    name = "edcs_identifier"
    verbose_name = "Edcs Identifier"
    identifier_modulus = 7
    messages_written = False
    include_in_administration_section = True

    def ready(self):
        if not self.messages_written:
            sys.stdout.write(f"Loading {self.verbose_name} ...\n")
            sys.stdout.write(f" * check-digit modulus: {self.identifier_modulus}\n")
            sys.stdout.write(f" Done loading {self.verbose_name}\n")
        self.messages_written = True


if settings.APP_NAME == "edcs_identifier":
    from edcs_device.apps import AppConfig as BaseEdcDeviceAppConfig
    from edcs_device.constants import CLIENT


    class EdcsDeviceAppConfig(BaseEdcDeviceAppConfig):
        device_role = CLIENT
        device_id = "14"

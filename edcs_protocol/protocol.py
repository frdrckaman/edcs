import pdb

import arrow
from dateutil.relativedelta import relativedelta
from django.conf import settings
from edcs_utils import get_utcnow

from .address import Address


class EdcsProtocolError(Exception):
    pass


class Protocol:
    """Encapsulates settings attributes:
    EDCS_PROTOCOL: 6 digit alpha-numeric
    EDCS_PROTOCOL_INSTITUTION_NAME
    EDCS_PROTOCOL_NUMBER: Used for identifiers NNN
    EDCS_PROTOCOL_PROJECT_NAME: Short name
        e.g. META, INTE, etc
    EDCS_PROTOCOL_STUDY_CLOSE_DATETIME
    EDCS_PROTOCOL_STUDY_OPEN_DATETIME
    EDCS_PROTOCOL_TITLE: Long name
    EMAIL_CONTACTS
    """

    def __init__(self):
        """Set with example defaults, you will need to change from your project"""

        self.protocol = getattr(settings, "EDCS_PROTOCOL", "AAA000")

        # 3 digits, used for identifiers, required for live systems
        self.protocol_number = getattr(settings, "EDCS_PROTOCOL_NUMBER", "000")
        # pdb.set_trace()
        if not settings.DEBUG and self.protocol_number == "000":
            raise EdcsProtocolError(
                "Settings attribute `EDCS_PROTOCOL_NUMBER` not defined or "
                "set to '000' while DEBUG=False."
            )

        self.protocol_title = getattr(
            settings, "EDCS_PROTOCOL_TITLE", "Protocol Title (set EDCS_PROTOCOL_TITLE)"
        )

        self.email_contacts = getattr(settings, "EMAIL_CONTACTS", {})

        self.institution = getattr(
            settings,
            "EDCS_PROTOCOL_INSTITUTION_NAME",
            "Institution (set EDCS_PROTOCOL_INSTITUTION_NAME)",
        )

        self.project_name = getattr(
            settings,
            "EDCS_PROTOCOL_PROJECT_NAME",
            "Project Name (set EDCS_PROTOCOL_PROJECT_NAME)",
        )
        self.protocol_name = self.project_name
        self.disclaimer = "For research purposes only."
        self.copyright = f"2020-{get_utcnow().year}"
        self.license = "GNU GENERAL PUBLIC LICENSE V3"

        self.default_url_name = "home_url"
        self.physical_address = Address()
        self.postal_address = Address()

        self.subject_identifier_pattern = getattr(
            settings,
            "EDCS_PROTOCOL_SUBJECT_IDENTIFIER_PATTERN",
            f"{self.protocol_number}\-[0-9\-]+",  # noqa
        )
        self.screening_identifier_pattern = getattr(
            settings, "EDCS_PROTOCOL_SCREENING_IDENTIFIER_PATTERN", "[A-Z0-9]{8}"
        )

        study_open_datetime = getattr(
            settings,
            "EDCS_PROTOCOL_STUDY_OPEN_DATETIME",
            arrow.utcnow().floor("hour") - relativedelta(months=1),
        )

        study_close_datetime = getattr(
            settings,
            "EDCS_PROTOCOL_STUDY_CLOSE_DATETIME",
            arrow.utcnow().ceil("hour") + relativedelta(years=1),
        )
        self.rstudy_open = (
            arrow.Arrow.fromdatetime(study_open_datetime, study_open_datetime.tzinfo)
            .to("utc")
            .floor("hour")
        )
        self.rstudy_close = (
            arrow.Arrow.fromdatetime(study_close_datetime, study_close_datetime.tzinfo)
            .to("utc")
            .ceil("hour")
        )
        self.study_open_datetime = self.rstudy_open.datetime
        self.study_close_datetime = self.rstudy_close.datetime

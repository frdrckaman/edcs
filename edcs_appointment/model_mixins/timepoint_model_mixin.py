from django.db import models

from ..choices import TIMEPOINT_STATUS
from ..constants import CLOSED_TIMEPOINT, FEEDBACK, OPEN_TIMEPOINT, NEW_TIMEPOINT


class UnableToCloseTimepoint(Exception):
    pass


class TimepointLookupModelMixin(models.Model):

    """Makes a model lookup the timepoint model instance on `save`
    and check if it is a closed before allowing a create or update.

    Note: the timepoint model uses the TimepointModelMixin, e.g. Appointment
    """


class TimepointModelMixin(models.Model):

    """Makes a model serve as a marker for a timepoint, e.g. Appointment."""

    enabled_as_timepoint = True

    timepoint_status = models.CharField(
        max_length=15, choices=TIMEPOINT_STATUS, default=NEW_TIMEPOINT
    )

    timepoint_opened_datetime = models.DateTimeField(
        null=True,
        editable=False,
        help_text="the original calculated model's datetime, updated in the signal",
    )

    timepoint_closed_datetime = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
       #TODO Codes to overide save methode
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

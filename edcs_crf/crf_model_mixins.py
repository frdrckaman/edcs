from django.contrib.sites.managers import CurrentSiteManager
from django.db import models

from edcs_model.models import HistoricalRecords


class CrfModelMixin(models.Model):

    # on_site = CurrentSiteManager()
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

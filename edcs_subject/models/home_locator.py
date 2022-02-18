from django.db import models

from edcs_model import models as edcs_models
from edcs_utils import get_utcnow

from ..model_mixins import CrfModelMixin


class HomeLocator(CrfModelMixin, edcs_models.BaseUuidModel):
    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )

    ward = models.CharField(
        verbose_name="Ward",
        max_length=45,
    )
    village = models.CharField(
        verbose_name="Village",
        max_length=45,
    )
    street = models.CharField(
        verbose_name="Street",
        max_length=45,
    )
    Kitongoji = models.CharField(
        verbose_name="Kitongoji",
        max_length=45,
    )
    Kitongoji_leader = models.CharField(
        verbose_name="Name of the Kitongoji leader",
        max_length=85,
    )
    nearest_church_mosque = models.CharField(
        verbose_name="Name of the nearest church and mosque",
        max_length=45,
    )
    nearest_healthcare_facility = models.CharField(
        verbose_name="Name of the nearest healthcare facility",
        max_length=125,
    )
    famous_person = models.CharField(
        verbose_name="Name of any person who is famous residing in the neighborhood",
        max_length=125,
    )
    famous_thing = models.CharField(
        verbose_name="Name of anything that is famous found in the neighborhood",
        max_length=125,
    )
    patient_phone_number = models.CharField(
        verbose_name="Phone number of the patient",
        max_length=45,
    )
    member_phone_number = models.TextField(
        verbose_name="Phone number of up to three members of the household",
        max_length=125,
    )
    close_relatives_phone_number = models.CharField(
        verbose_name="Phone numbers of other two close relatives",
        max_length=125,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Home Locator Form"
        verbose_name_plural = "Home Locator Form"

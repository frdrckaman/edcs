from django.db import models

from edcs_model import models as edcs_models


class DataDownload(edcs_models.BaseUuidModel):
    username = models.CharField(
        verbose_name="Username",
        max_length=25,
    )

    first_name = models.CharField(
        verbose_name="First Name",
        max_length=45,
    )

    last_name = models.CharField(
        verbose_name="Last Name",
        max_length=45,
    )

    email = models.CharField(
        verbose_name="Email Address",
        max_length=85,
    )

    data_type = models.CharField(
        verbose_name="Data Type",
        max_length=85,
    )

    class Meta(edcs_models.BaseUuidModel.Meta):
        verbose_name = "Data Download"
        verbose_name_plural = "Data Download"

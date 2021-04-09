from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.deletion import CASCADE
from django.contrib.sites.models import Site


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name='profile')
    job_title = models.CharField(max_length=100, null=True, blank=True)
    alternate_email = models.EmailField("Alternate email address", blank=True, null=True)
    sites = models.ManyToManyField(Site, blank=True)
    mobile = models.CharField(max_length=25, validators=[RegexValidator(regex="^\+\d+")], null=True, blank=True,
                              help_text="e.g. +1234567890")

    def __str__(self):
        return self.user.username

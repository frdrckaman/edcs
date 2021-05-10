import sys

from django.db import models
from django.conf import settings
from django_audit_fields.models import AuditUuidModelMixin


class Device(AuditUuidModelMixin, models.Model):
    pass




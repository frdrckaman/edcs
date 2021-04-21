from django.conf import settings
from .address_mixin import AddressMixin
from .base_model import BaseModel
from .base_uuid_model import BaseUuidModel
from .historical_records import HistoricalRecords
from .url_model_mixin import UrlModelMixin, UrlModelMixinNoReverseMatch


if settings.APP_NAME == "edcs_model":
    from ..tests.models import *  # noqa

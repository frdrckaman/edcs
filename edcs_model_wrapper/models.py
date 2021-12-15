from django.conf import settings

if settings.APP_NAME == "edcs_model_wrapper":
    from .tests import models  # noqa

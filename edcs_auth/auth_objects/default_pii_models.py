from django.conf import settings

default_pii_models = [
    settings.SUBJECT_CONSENT_MODEL,
    # "edcs_locator.subjectlocator",
    "edcs_registration.registeredsubject",
]

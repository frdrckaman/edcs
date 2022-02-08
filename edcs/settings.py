import os
from pathlib import Path

import environ
from multisite import SiteID

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from edcs_utils import get_datetime_from_env

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    DJANGO_EDCS_BOOTSTRAP=(int, 3),
    DATABASE_SQLITE_ENABLED=(bool, False),
    DJANGO_EMAIL_ENABLED=(bool, False),
    DJANGO_AUTO_CREATE_KEYS=(bool, False),
)

environ.Env.read_env(ENV_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

APP_NAME = env.str("DJANGO_APP_NAME")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

DEBUG_TOOLBAR = env("DEBUG_TOOLBAR")

SUBJECT_DATA_MODEL = env("EDCS_SUBJECT_DATA_MODEL")

LOGIN_REDIRECT_URL = env.str("DJANGO_LOGIN_REDIRECT_URL")

EDCS_BOOTSTRAP = env("DJANGO_EDCS_BOOTSTRAP")

DASHBOARD_BASE_TEMPLATES = env.dict("DJANGO_DASHBOARD_BASE_TEMPLATES")

SUBJECT_SCREENING_MODEL = env.str("EDCS_SUBJECT_SCREENING_MODEL")

SUBJECT_CONSENT_MODEL = env.str("EDCS_SUBJECT_CONSENT_MODEL")

SUBJECT_VISIT_MODEL = env.str("EDCS_SUBJECT_VISIT_MODEL")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_revision.apps.AppConfig",
    "django_audit_fields.apps.AppConfig",
    "logentry_admin",
    "defender",
    "multisite",
    "simple_history",
    "django_crypto_fields.apps.AppConfig",
    "edcs_auth.apps.AppConfig",
    "edcs_dashboard.apps.AppConfig",
    "edcs_device.apps.AppConfig",
    "edcs_model.apps.AppConfig",
    "edcs_identifier.apps.AppConfig",
    "edcs_list_data.apps.AppConfig",
    "edcs_lists.apps.AppConfig",
    "edcs_screening.apps.AppConfig",
    "edcs_subject.apps.AppConfig",
    "edcs_consent.apps.AppConfig",
    "edcs_registration.apps.AppConfig",
    "edcs_notification.apps.AppConfig",
    "edcs_visit_schedule.apps.AppConfig",
    "edcs_export.apps.AppConfig",
    "edcs_sites.apps.AppConfig",
    "edcs_facility.apps.AppConfig",
    "edcs_appointment.apps.AppConfig",
    "edcs_crf.apps.AppConfig",
]

MIDDLEWARE = [
    "multisite.middleware.DynamicSiteMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.contrib.sites.middleware.CurrentSiteMiddleware'
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

MIDDLEWARE.extend(
    [
        "edcs_dashboard.middleware.DashboardMiddleware",
    ]
)

ROOT_URLCONF = "edcs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "edcs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if env.str("DJANGO_CACHE") == "redis":
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "PASSWORD": env.str("DJANGO_REDIS_PASSWORD"),
            },
            "KEY_PREFIX": f"{APP_NAME}",
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"
    DJANGO_REDIS_IGNORE_EXCEPTIONS = True
    DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True
elif env.str("DJANGO_CACHE") == "memcached":
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
            "LOCATION": "unix:/tmp/memcached.sock",
        }
    }
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

EDCS_APPOINTMENT_INTERVAL = env("EDCS_APPOINTMENT_INTERVAL")
EDCS_PROTOCOL = env.str("EDCS_PROTOCOL")
EDCS_PROTOCOL_TITLE = env.str("EDCS_PROTOCOL_TITLE")
EDCS_PROTOCOL_NUMBER = env.str("EDCS_PROTOCOL_NUMBER")
EDCS_PROTOCOL_INSTITUTION_NAME = env.str("EDCS_PROTOCOL_INSTITUTION_NAME")
EDCS_PROTOCOL_PROJECT_NAME = env.str("EDCS_PROTOCOL_PROJECT_NAME")
EDCS_PROTOCOL_STUDY_OPEN_DATETIME = get_datetime_from_env(
    *env.list("EDCS_PROTOCOL_STUDY_OPEN_DATETIME")
)
EDCS_PROTOCOL_STUDY_CLOSE_DATETIME = get_datetime_from_env(
    *env.list("EDCS_PROTOCOL_STUDY_CLOSE_DATETIME")
)

KEY_PATH = env.str("DJANGO_KEY_FOLDER")

ETC_DIR = env.str("DJANGO_ETC_FOLDER")

AUTO_CREATE_KEYS = env("DJANGO_AUTO_CREATE_KEYS")

EMAIL_ENABLED = env("DJANGO_EMAIL_ENABLED")

GIT_DIR = BASE_DIR

APP_NAME = env.str("DJANGO_APP_NAME")

ACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

DEFENDER_REDIS_NAME = "default"
DEFENDER_LOCK_OUT_BY_IP_AND_USERNAME = True
DEFENDER_LOCKOUT_TEMPLATE = "edcs_auth/bootstrap3/login.html"
DEFENDER_LOGIN_FAILURE_LIMIT = 5

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = SiteID(default=1)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

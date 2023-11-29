"""
Django settings for {{ cookiecutter.project_slug }} project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

For a checklist on production-ready settings, see
https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

For details about what is already configured, see
https://github.com/fsinfuhh/template

In addition to configuring django, this file also takes in settings at runtime via environment variables.
This is done in the following order of precedence:
- Taken from the actual program environment
- Read from a .env file
- Read from a .env.local file
- Read from a .env.$mode file (e.g. env.dev or .env.prod)
- Read from a .env.$mode.local file (e.g. .env.dev.local or .env.prod.local)
"""

from pathlib import Path

from environs import Env

# Build paths inside the project like this: PROJ_DIR / 'subdir'.
SRC_DIR = Path(__file__).resolve().parent.parent
PROJ_DIR = SRC_DIR.parent

# Access runtime settings via `MY_SETTING = env.str("MY_SETTING")` (or user other types e.g. `env.bool()`)
env = Env()
env.read_env(".env", override=True)
env.read_env(".env.local", override=True)
APP_MODE = env.str("APP_MODE", default="dev")
env.read_env(f".env.{APP_MODE}", override=True)
env.read_env(f".env.{APP_MODE}.local", override=True)

# general django settings based on runtime config
DEBUG = env.bool("DJANGO_DEBUG", default=False)
SECRET_KEY = env.str("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")
DATABASES = {"default": env.dj_db_url("DJANGO_DB")}
CACHES = {"default": env.dj_cache_url("DJANGO_CACHE", default="locmem://default")}
CORS_ALLOWED_ORIGINS = env.list("DJANGO_ALLOWED_CORS_ORIGINS", default=[])

# openid authentication
OPENID_CLIENT_ID = env.str("DJANGO_OPENID_CLIENT_ID")
OPENID_CLIENT_SECRET = env.str("DJANGO_OPENID_CLIENT_SECRET")
OPENID_ISSUER = env.str("OPENID_ISSUER", default="https://identity.mafiasi.de/realms/mafiasi")
OPENID_SCOPE = "{{ cookiecutter.openid_scope }}"
OPENID_USER_MAPPER = "{{ cookiecutter.project_slug }}.core.oidc_user_mapping.MafiasiUserMapper"
OPENID_ANY_USER_IS_ADMIN = env.bool("DJANGO_ANY_OPENID_USER_IS_ADMIN", default=False)
OPENID_SUPERUSER_GROUPS = env.list("DJANGO_OPENID_SUPERUSER_GROUPS", default=[])



# static django config

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "simple_openid_connect.integrations.django",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "{{ cookiecutter.project_slug }}.core",
    "{{ cookiecutter.project_slug }}.api",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"

AUTH_USER_MODEL = "{{ cookiecutter.project_slug }}_core.MafiasiUser"
LOGIN_REDIRECT_URL = "/"
OPENID_REDIRECT_URI = None

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = SRC_DIR / "django-staticfiles"
STATIC_URL = "django-static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Api Framework Settings
# https://www.django-rest-framework.org/api-guide/settings/
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "simple_openid_connect.integrations.djangorestframework.authentication.AccessTokenAuthentication",
    ],
}

from {{cookiecutter.project_slug}} import __author__ as app_author
from {{cookiecutter.project_slug}} import __version__ as app_version

SPECTACULAR_SETTINGS = {
    "TITLE": "{{ cookiecutter.project_name }} API",
    "VERSION": app_version,
    "CONTACT": {
        "name": app_author
    },
    "LICENSE": {
        "name": "MIT",
    },
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "COMPONENT_SPLIT_REQUEST": True,
    "AUTHENTICATION_WHITELIST": [
        "simple_openid_connect.integrations.djangorestframework.authentication.AccessTokenAuthentication",
    ],
}

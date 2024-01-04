from .base import *

APP_ENV = 'prod'

DEBUG = False

ALLOWED_HOSTS = ['https://google.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 300,  # 기본값 300초 = 5분
        'OPTIONS': {'MAX_ENTRIES': 300},  # 기본값 = 300
    }
}

INSTALLED_APPS += [
    "",
]

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {},
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {},
    },
}

from .base import *

APP_ENV = 'dev'

DEBUG = True

ALLOWED_HOSTS = ['*']

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
    "django_extensions",
]

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "AWS_S3_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
            "AWS_S3_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
            "AWS_S3_REGION_NAME": AWS_S3_REGION_NAME,
            "AWS_S3_CUSTOM_DOMAIN": AWS_S3_CUSTOM_DOMAIN,
            "AWS_STORAGE_BUCKET_NAME": AWS_STORAGE_BUCKET_NAME,
            "AWS_LOCATION": f"{APP_ENV}/media",
            "AWS_DEFAULT_ACL": "public-read",
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        "OPTIONS": {},
    },
}

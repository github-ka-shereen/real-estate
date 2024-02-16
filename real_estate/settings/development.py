from .base import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '20f4126f9cf4ad'
EMAIL_HOST_PASSWORD = '0c89f108737f5b'
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL = "info@aewebsites.co.zw"
DOMAIN = "localhost:8000"
SITE_NAME = "Real Estate"


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}



CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = "Africa/Harare"

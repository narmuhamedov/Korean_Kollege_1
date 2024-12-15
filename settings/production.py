from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = [
    "kkc.kg",
    "www.kkc.kg",
    "127.0.0.1",
    "localhost",
    "saving-randomly-malamute.ngrok-free.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://saving-randomly-malamute.ngrok-free.app",
    "https://translate.googleapis.com",
    "https://127.0.0.1",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("SQL_DB", "db"),
        "USER": os.getenv("SQL_USER", "user"),
        "PASSWORD": os.getenv("SQL_PASSWORD", "password"),
        "HOST": os.getenv("SQL_HOST", "localhost"),
        "PORT": os.getenv("SQL_PORT", "5432"),
    }
}

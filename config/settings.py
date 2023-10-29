from datetime import timedelta
import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default=get_random_secret_key())
DEBUG = os.getenv("DEBUG", default="False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1").split(", ")
CSRF_TRUSTED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")
CORS_ALLOWED_ORIGINS = os.getenv("TRUSTED_ORIGINS", default="").split(", ")

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "djoser",
    "drf_spectacular",
    "corsheaders",
]

LOCAL_APPS = [
    "apps.users.apps.UsersConfig",
    "apps.employers.apps.EmployersConfig",
    "apps.vacancies.apps.VacanciesConfig",
    "apps.students.apps.StudentsConfig",
    "apps.attributes.apps.AttributesConfig",
    "apps.core.apps.CoreConfig",
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

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

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", default="postgres"),
        "USER": os.getenv("POSTGRES_USER", default="postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="postgres"),
        "HOST": os.getenv("POSTGRES_HOST", default="db"),
        "PORT": os.getenv("POSTGRES_PORT", default=5432),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

LANGUAGE_CODE = "ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DATE_FORMAT": "%d.%m.%Y",
    "DATETIME_FORMAT": "%d.%m.%Y %H:%M",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "API для сервиса подбора резюме. Команда Seven-Eleven (11)",
    "DESCRIPTION": "Проект разработан в рамках Яндекс-Хакатона: Карьерный трекер. Резюме",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

DJOSER = {
    "SERIALIZERS": {
        "user_create": "apps.api.v1.users.serializers.MyUserCreateSerializer",
        "current_user": "apps.api.v1.users.serializers.MeUserSerializer",
    },
    "HIDE_USERS": True,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1 * 24 * 5),  # пока пишем код
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("JWT",),
}

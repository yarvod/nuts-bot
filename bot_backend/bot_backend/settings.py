from pathlib import Path
import os
import sys

from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key())
TOKEN = os.getenv('TOKEN')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

ALLOWED_HOSTS = ['*']
HOST = os.environ.get('HOST')
HTTP = os.environ.get('HTTP')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'psycopg2',
    'corsheaders',
    'django_extensions',
    'imagekit',
    'rest_framework',
    'storages',

    'bot',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bot_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bot_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'db_name'),
        'USER': os.environ.get('POSTGRES_USER', 'db_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'db_password'),
        'HOST': os.environ.get('DB_HOST', 'postgres_db'),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db.sqlite3'
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

MEDIA_PREFIX = f"{HTTP}://{HOST}" if DEBUG else ''

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname) -4s %(name) -2s [%(pathname)s:%(lineno)d] %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(levelname) -4s %(name) -2s [%(filename)s:%(lineno)d] %(message)s'
        }
    },
    "handlers": {
        "console": {
            'level': 'INFO',
            "class": "logging.StreamHandler",
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': f'{BASE_DIR}/total.log'
        }
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ['console', 'file']
        },
    },
}

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    f"http://localhost:8080",
    f"{HTTP}://{HOST}"
]
X_FRAME_OPTIONS = 'SAMEORIGIN'


# STORAGE

YANDEX_BUCKET_NAME = os.environ.get('YANDEX_BUCKET_NAME')
AWS_S3_ACCESS_KEY_ID = os.environ.get('YANDEX_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('YANDEX_SECRET_ACCESS_KEY')
AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
AWS_S3_REGION_NAME = os.environ.get('YANDEX_BUCKET_NAME')

USE_S3 = os.getenv('USE_S3', 'false').lower() == 'true'
DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
if USE_S3:
    DEFAULT_FILE_STORAGE = 'bot_backend.storage.UsersMediaStorage'


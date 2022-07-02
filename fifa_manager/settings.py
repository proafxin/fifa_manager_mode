"""
Django settings for fifa_manager project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ['FIFA_MANAGER_DJANGO_SECRET_KEY']

MAX_OFFER_ITERATION = 3
TRANSFER_WINDOW_DAYS = 30
PLAYER_SELL_EMBARGO_DAYS = 180
MAX_LENGTH = 100
DEFAULT_PLAYER_VALUE = 1000000
DEFAULT_BUDGET = 5*DEFAULT_PLAYER_VALUE
DEFAULT_INITIAL_PLAYER_NUMBER = 20
DEFAULT_VALUE = DEFAULT_PLAYER_VALUE*DEFAULT_INITIAL_PLAYER_NUMBER

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'debug_toolbar',
    'coreapi',
    'drf_yasg',
    'silk',
    'manager',
]

AUTH_USER_MODEL = 'manager.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

LOGIN_REDIRECT_URL = 'team-list'
LOGIN_URL = 'api-auth/login/'
LOGOUT_URL = 'api-auth/logout/'
LOGOUT_REDIRECT_URL = 'api-auth/login/'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'LOGIN_URL': LOGIN_URL,
    'LOGIN_REDIRECT_URL': LOGIN_REDIRECT_URL,
    'LOGOUT_URL': LOGOUT_URL,
}



ROOT_URLCONF = 'fifa_manager.urls'

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

WSGI_APPLICATION = 'fifa_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASE_NAME = environ['FIFA_MANAGER_MYSQL_DATABASE_NAME']
DATABASE_USERNAME = environ['MYSQL_USERNAME']
DATABASE_HOST = environ['MYSQL_HOST']
DATABASE_PASSWORD = environ['MYSQL_PASSWORD']
DATABASE_PORT = environ['MYSQL_PORT']

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'database': DATABASE_NAME,
            'host': DATABASE_HOST,
            'user': DATABASE_USERNAME,
            'password': DATABASE_PASSWORD,
            'port': int(DATABASE_PORT),
        },
    },
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

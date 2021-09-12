from os import environ
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = environ.get('DEBUG')
if DEBUG is None:
    DEBUG = False
else:
    DEBUG = DEBUG.lower().strip() not in ['', '0', 'false', 'no']

SECRET_KEY = environ.get('SECRET_KEY')
if not SECRET_KEY and DEBUG:
    SECRET_KEY = 'secret'

ALLOWED_HOSTS = [host for host in environ.get('ALLOWED_HOSTS', '').split(':') if host] or ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webprint',
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

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'project' / 'templates',
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///%s' % (BASE_DIR / 'db.sqlite3'), conn_max_age=600),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

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

LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en-us')
TIME_ZONE = environ.get('TIME_ZONE', 'UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = [
    BASE_DIR / 'project' / 'static',
]
STATIC_ROOT = Path(environ.get('STATIC_ROOT', BASE_DIR / 'staticfiles')).resolve()
STATIC_URL = '/static/'
MEDIA_ROOT = Path(environ.get('MEDIA_ROOT', BASE_DIR / 'mediafiles')).resolve()
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

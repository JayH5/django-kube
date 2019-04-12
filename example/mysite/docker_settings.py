# An example settings file for deploying a Django app in a Docker container.
# Uses environment variables to configure the majority of settings. This
# pattern is sometimes attributed to the '12factor' app guidelines:
# https://12factor.net/config

import os

# Import the existing settings file, we'll work from there...
from .settings import ALLOWED_HOSTS, SECRET_KEY
from .settings import *


def parse_bool(string):
    # Port of golang's strconv.ParseBool function
    # https://golang.org/pkg/strconv/#ParseBool
    if string in ['1', 't', 'T', 'true', 'TRUE', 'True']:
        return True
    elif string in ['0', 'f', 'F', 'false', 'FALSE', 'False']:
        return False

    raise ValueError("Unable to parse boolean value from '{}'".format(string))


def parse_list(string):
    return [s for s in string.split(',') if s]


def environ_get(key, default=None, parser=None, environ=os.environ):
    val = environ.get(key)
    if val is None:
        return default

    if parser is not None:
        val = parser(val)

    return val


SECRET_KEY = environ_get('SECRET_KEY', default=SECRET_KEY)
DEBUG = environ_get('DEBUG', parser=parse_bool, default=False)
ALLOWED_HOSTS = environ_get(
    'ALLOWED_HOSTS', parser=parse_list, default=ALLOWED_HOSTS)

DATABASES = {
    'default': {
        'ENGINE': environ_get('DATABASE_ENGINE',
                              default='django.db.backends.postgresql'),
        'NAME': environ_get('DATABASE_NAME'),
        'USER': environ_get('DATABASE_USER'),
        'PASSWORD': environ_get('DATABASE_PASSWORD'),
        'HOST': environ_get('DATABASE_HOST'),
        'PORT': environ_get('DATABASE_PORT', default='5432'),
    }
}

# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

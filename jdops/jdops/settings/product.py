# coding:utf-8

from .base import *  # noqa


DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autoops',
        'PASSWORD': 'xxxxx',
    }
}

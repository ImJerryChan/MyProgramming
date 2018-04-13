# coding:utf-8

from .base import *  # noqa


DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jdops',
        'USER': 'root',
        'PASSWORD': 'mylovely5213',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

REDIS_SSEQUEUE_CONNECTION_SETTINGS = {
    'location': '127.0.0.1:6379',
    'db': 0,
}


log_path = BASE_DIR

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'info.log'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10,
            'formatter': 'default',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(log_path, 'error.log'),
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 10,
            'formatter': 'default',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_info'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_error'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

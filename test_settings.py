"""
Simplest possible settings.py for use in running django_highrise unit tests.

This settings file would be completely useless for running a project, however
it has enough in it to be able to run the django unit test runner, and to spin
up django.contrib.auth users (as required by django_highrise).

In order for the tests to run, you will need to set the following environment
variables: HIGHRISE_SERVER and HIGHRISE_API_KEY.

Please see online documentation for more details.
"""
from os import environ as env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'delme'
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'errordite'
)

ERRORDITE_TOKEN = env.get('ERRORDITE_TOKEN', None)

if ERRORDITE_TOKEN is None:
    raise Exception("You must set the ERRORDITE_TOKEN environment "
                    "variable if you wish to run the tests.")

# this isn't used, however the django_highrise app does reference a logger,
# so although the tests will run without this, some warnings will appear.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'errordite': {
            'level': 'DEBUG',
            'class': 'errordite.ErrorditeHandler',
            'token': ERRORDITE_TOKEN,
            'formatter': 'simple'
        },
        'django_errordite': {
            'level': 'DEBUG',
            'class': 'errordite.contrib.DjangoErrorditeHandler',
            'token': ERRORDITE_TOKEN,
            'formatter': 'simple'
        },
    },
    'loggers': {
        'errordite_logger': {
            'handlers': ['errordite', 'django_errordite'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}

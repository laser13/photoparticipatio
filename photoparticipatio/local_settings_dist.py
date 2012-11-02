__author__ = 'G@mOBEP'

from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES

DEBUG = True
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':     '',                         # Or path to database file if using sqlite3.
        'USER':     '',                         # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST':     '',                         # Set to empty string for localhost. Not used with sqlite3.
        'PORT':     '',                         # Set to empty string for default. Not used with sqlite3.
    }
}

#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)
#
#INTERNAL_IPS = ('127.0.0.1',)
#
#INSTALLED_APPS += (
#    'debug_toolbar',
#)
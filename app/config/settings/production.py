from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
]
WSGI_APPLICATION = 'config.wsgi.production.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'

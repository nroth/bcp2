from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# I'm not so worried about keeping it secret on my dev machine
SECRET_KEY = 'wow-now-you-know-my-secret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'compass.db',
    }
}

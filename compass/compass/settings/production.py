import os
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# get the secret key from an environment variable
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(PROJECT_ROOT, "mysql.cnf"),
        },
    }
}

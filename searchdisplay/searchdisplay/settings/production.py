# settings/production.py
import os
from .base import *

DEBUG = False
debug_level = 'INFO'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DBENGINE','django.db.backends.postgresql'),
        'NAME': os.getenv('DBNAME','unsetdbname'),
        'USER': os.getenv('DBUSER','unsetdbuser'),
        'PASSWORD': os.getenv('DBPASS','unsetdbpass'),
        'HOST': os.getenv('DBHOST','unsetdbhost'),
        'PORT': os.getenv('DBPORT','unsetdbport'),
    }
}
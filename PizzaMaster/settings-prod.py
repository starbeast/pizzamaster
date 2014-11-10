import os
from PizzaMaster.settings import *
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles/')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
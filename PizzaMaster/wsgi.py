"""
WSGI config for PizzaMaster project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PizzaMaster.settings")
if settings.DEBUG:
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()
    application = DjangoWhiteNoise(application)

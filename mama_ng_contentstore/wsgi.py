"""
WSGI config for mama_ng_control project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "mama_ng_contentstore.settings")

from dj_static import Cling, MediaCling
application = Cling(MediaCling(get_wsgi_application()))

"""
WSGI config for django_mama_ng project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "django_mama_ng.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

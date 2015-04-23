from django_mama_ng.settings import *  # flake8: noqa

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@localhost/django_mama_ng'),
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TESTSEKRET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

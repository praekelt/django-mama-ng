#!/bin/sh

export DJANGO_SETTINGS_MODULE="django_mama_ng.testsettings"
cd django_mama_ng
py.test django_mama_ng/tests.py "$@"

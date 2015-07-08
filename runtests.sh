#!/bin/sh

export DJANGO_SETTINGS_MODULE="mama_ng_contentstore.testsettings"
py.test mama_ng_contentstore/tests.py "$@"

# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import django
from django.conf import settings


def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_settings")
    if settings.configured and hasattr(django, 'setup'):
        django.setup()

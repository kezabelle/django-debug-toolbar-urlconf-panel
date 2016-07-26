# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from debug_toolbar_urlspanel.views import urls_list
from django.conf.urls import url

urls_view = url("^$", urls_list, name="debug_toolbar_urlspanel")

urlpatterns = [
    urls_view,
]

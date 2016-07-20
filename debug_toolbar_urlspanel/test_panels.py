# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from .panels import UrlsPanel

def test_executes():
    panel = UrlsPanel(toolbar=None)
    assert panel.title == 'URLs'

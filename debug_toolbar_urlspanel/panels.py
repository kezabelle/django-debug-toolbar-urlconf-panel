# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from debug_toolbar.panels import Panel
from django.conf import settings
from debug_toolbar_urlspanel.fetch import get_urls

class UrlsPanel(Panel):
    title = "URLs"
    nav_subtitle = "Project's urlconfs"
    template = "debug_toolbar/panels/urls.html"

    def get_stats(self):
        urls = tuple(get_urls(settings.ROOT_URLCONF))
        namespaces = ()
        # namespaces = sorted(set(x['namespace_string'] for x in urls))
        return {'urlconf': urls, 'namespaces': namespaces}

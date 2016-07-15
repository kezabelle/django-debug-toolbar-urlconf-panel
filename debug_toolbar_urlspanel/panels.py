# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django
from django.contrib.admindocs.views import (simplify_regex, named_group_matcher,
                                            non_named_group_matcher)

try:
    from importli2 import import_module
except ImportError:
    from django.utils.importlib import import_module

from debug_toolbar.panels import Panel
from django.conf import settings


if django.VERSION[0:2] > (1, 7):
    from django.contrib.admindocs.views import extract_views_from_urlpatterns
else:
    from django.utils.translation import ugettext as _
    from django.core.exceptions import ViewDoesNotExist
    def extract_views_from_urlpatterns(urlpatterns, base='', namespace=None):
        # taken from 16a842b3795ca78a5918538ab6b9f1afbd718f72
        views = []
        for p in urlpatterns:
            if hasattr(p, 'url_patterns'):
                try:
                    patterns = p.url_patterns
                except ImportError:
                    continue
                views.extend(extract_views_from_urlpatterns(
                    patterns,
                    base + p.regex.pattern,
                    (namespace or []) + (p.namespace and [p.namespace] or [])
                ))
            elif hasattr(p, 'callback'):
                try:
                    views.append((p.callback, base + p.regex.pattern,
                                  namespace, p.name))
                except ViewDoesNotExist:
                    continue
            else:
                raise TypeError(_("%s does not appear to be a urlpattern object") % p)
        return views

def get_urls(urlconf_name):
    urlconf = import_module(urlconf_name)
    all_urls = extract_views_from_urlpatterns(urlconf.urlpatterns)
    for mounted_url in all_urls:
        viewfunc = mounted_url[0]
        regex = mounted_url[1]
        try:
            namespace = mounted_url[2]
        except IndexError:
            namespace = None
        try:
            name = mounted_url[3]
        except IndexError:
            name = None
        modname = viewfunc.__module__
        viewname = getattr(viewfunc, '__name__', viewfunc.__class__.__name__)
        simple_url = simplify_regex(regex)
        named_groups = named_group_matcher.findall(regex)
        yield {
            'module': modname,
            'view': viewname,
            'url': simple_url,
            'namespace': namespace,
            'name': name,
            'named_url_kwargs': named_groups,
            'unnamed_url_args': (),
        }


class UrlsPanel(Panel):
    title = "URLs"
    nav_subtitle = "Project's urlconfs"
    template = "debug_toolbar/panels/urls.html"

    def get_stats(self):
        urls = tuple(get_urls(settings.ROOT_URLCONF))
        return {'urlconf': urls}

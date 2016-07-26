# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.template.response import TemplateResponse
from debug_toolbar_urlspanel.fetch import get_urls_filtered
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from itertools import chain


@login_required
def urls_list(request):
    if not hasattr(request.user, 'is_superuser') or request.user.is_superuser is False:
        raise PermissionDenied("Non superuser attempted to list all URLs")
    template = "debug_toolbar_urlspanel/urls_list.html"
    args = (x.split(" ") for x in request.GET.getlist('s'))
    args = tuple(x for x in chain.from_iterable(args) if x.strip() != "")
    urlconf = get_urls_filtered(urlconf_name=settings.ROOT_URLCONF, filters=args)
    context = {
        'urlconf': urlconf,
        'args': " ".join(args),
    }
    return TemplateResponse(request=request, template=template, context=context)
urls_list.debug_toolbar_urlspanel = True

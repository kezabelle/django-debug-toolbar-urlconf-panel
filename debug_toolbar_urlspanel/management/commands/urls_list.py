# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import os
import sys
from django.core.management.base import BaseCommand
from pydoc import pipepager
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
try:
    from shutil import get_terminal_size
except ImportError:
    try:
        from backports.shutil_get_terminal_size import get_terminal_size
    except ImportError:
        def get_terminal_size():
            return 0, 1
from debug_toolbar_urlspanel.fetch import get_urls_filtered

class Command(BaseCommand):
    can_import_settings = True
    def handle(self, *args, **kwargs):
        from django.conf import settings
        all_urls = tuple(get_urls_filtered(urlconf_name=settings.ROOT_URLCONF, filters=args))
        output = StringIO()
        for url in all_urls:
            uri = "URL: " + self.style.HTTP_REDIRECT(url['url'])
            viewname = "{}.{}".format(url['module'], url['view'])
            view = "View: " + self.style.HTTP_NOT_MODIFIED(viewname)
            name = None
            namespace = ""
            if url['namespace']:
                for part in url['namespace']:
                    namespace += part + ":"
            if url['name']:
                name = "Name: " + self.style.HTTP_INFO(namespace + url['name'])
            arguments = None
            if url['named_url_kwargs']:
                arguments = "Arguments: " + self.style.HTTP_INFO(", ".join(url['named_url_kwargs']))
            linelength = "-" * (get_terminal_size()[0] or 20)

            lineparts = (uri, view, name, arguments, linelength + "\n")
            lines = "\n".join(part for part in lineparts if part is not None)
            output.write(lines)
        text = output.getvalue()
        output.close()
        if text:
            if hasattr(os, 'system') and os.system('(less) 2>/dev/null') == 0:
                return pipepager(text, 'less -R -i')
            else:
                return self.stdout.write(text)
        # no text, so error state.
        return sys.exit(1)

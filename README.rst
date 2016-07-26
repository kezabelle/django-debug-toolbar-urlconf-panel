django-debug-toolbar-urlconf-panel
==================================

:author: Keryn Knight
:version: 0.1.0

A `Django Debug Toolbar`_ panel for listing all the URLs which exist in a
`Django`_ project. Does much the same as `admindocs`_, but on a per-page basis.

As a "*bonus*", there is also a management command ``urls_list`` for printing them
all to the console, doing much the same as `django-extensions`_.

Getting started
---------------

You'll need to get the package onto your python path. For now, that's something like::

    pip install git+https://github.com/kezabelle/django-django-debug-toolbar-urlconf-panel.git#egg=django-debug-toolbar-urlconf-panel

You'll also need to ensure it's part of your ``INSTALLED_APPS``::

    INSTALLED_APPS += (
    'debug_toolbar_urlspanel',
)

Finally you'll need to add it to your ``DEBUG_TOOLBAR_PANELS``::

    DEBUG_TOOLBAR_PANELS = [
        # ...
        'debug_toolbar_urlspanel.panels.UrlsPanel',
        # ...
    ]

Assuming it all works, there should now be an additional panel available in
the `Django Debug Toolbar`_ titled **URLs**.

Features
--------

Filtering the panel's results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can filter the results by typing some lookup into the appropriate input box
in the panel. It should do partial matching on the module name, view name,
name defined via the ``url()`` and URL parts (split by ``/``)

Management command
^^^^^^^^^^^^^^^^^^
This is also true of the management command ``urls_list``, if used like so::

    python manage.py urls_list myapp otherapp

which should show anything including **either** of those labels. If you're using
an interactive shell and have ``less`` it'll try and use that as a pager, otherwise
it'll just print to whatever stdout is.

As a separate page
^^^^^^^^^^^^^^^^^^

If for some reason you want a URL like ``/urls/`` to list everything, you can
do that by adding the following to your urlconf::

urlpatterns = [
    # ...
    url(r'^urls/', include('debug_toolbar_urlspanel.urls')),
    # ...
]

The ``urls_list`` view contained within will list out all the same data the
panel does, for authenticated users (using ``@login_required``) with ``is_superuser=True``

Re-using it elsewhere
---------------------

Internally, ``django-debug-toolbar-urlconf-panel`` makes use of the same code
as `admindocs`_ but wrapped up to provide extra info, and a simple API.
If you need to get all URLs defined in the project for another purpose, there is
the function ``debug_toolbar_urlspanel.fetch.get_urls(urlconf_name="project.urls")``
which expects a string ``urlconf_name`` pointing at something which can be
imported as a urlconf. It will ``yield`` results until it completes or an exception
occurs.

There is an accompanying function, ``get_urls_filtered`` in the same module,
which takes an iterable (``tuple``, ``list`` etc.) of strings to partially or
completely match, and returns only the subset
which do (see the **Management command** section, which uses it)

Tests
-----

There aren't any. This was just an experiment which I've refined a touch because
I couldn't find a djdt panel for listing URLs.

Trust it or don't.

Supported versions
------------------

I had it execute without errors on Django **1.4** and **1.8** using
debug toolbar >= **1.3** ... so it probably works?

The license
-----------

It's the `FreeBSD`_. There's should be a ``LICENSE`` file in the root of the repository, and in any archives.

.. _FreeBSD: http://en.wikipedia.org/wiki/BSD_licenses#2-clause_license_.28.22Simplified_BSD_License.22_or_.22FreeBSD_License.22.29
.. _Django Debug Toolbar: https://github.com/django-debug-toolbar/django-debug-toolbar
.. _Django: https://www.djangoproject.com/
.. _admindocs: https://docs.djangoproject.com/en/stable/ref/contrib/admin/admindocs/
.. _django-extensions: http://django-extensions.readthedocs.io/en/latest/command_extensions.html?highlight=show_urls

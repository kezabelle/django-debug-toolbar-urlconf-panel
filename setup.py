#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from setuptools import setup
from setuptools.command.test import test as TestCommand
if sys.version_info[0] == 2:
    # get the Py3K compatible `encoding=` for opening files.
	from io import open


HERE = os.path.abspath(os.path.dirname(__file__))


class PyTest(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def make_readme(root_path):
    consider_files = ("README.rst", "LICENSE", "CHANGELOG", "CONTRIBUTORS")
    for filename in consider_files:
        filepath = os.path.realpath(os.path.join(root_path, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode="r", encoding="utf-8") as f:
                yield f.read()


LONG_DESCRIPTION = "\r\n\r\n----\r\n\r\n".join(make_readme(HERE))
SHORT_DESCRIPTION = "Django debug toolbar panel for listing all the URLs defined on a project, as per admindocs/django-extensions"
KEYWORDS = (
    "debug",
    "urlconf",
    "list",
    "toolbar",
)

setup(
    name="django-debug-toolbar-urlconf-panel",
    version="0.1.0",
    author="Keryn Knight",
    author_email="python-django-debug-toolbar-urlconf-panel@kerynknight.com",
    description=SHORT_DESCRIPTION[0:200],
    long_description=LONG_DESCRIPTION,
    packages=[
        "debug_toolbar_urlspanel",
    ],
    include_package_data=True,
    install_requires=[
        "Django>1.4.0",
        "django-debug-toolbar>=1.3.0",
    ],
    tests_require=[
        "pytest>=2.6",
        "pytest-cov>=1.8",
        "pytest-remove-stale-bytecode>=1.0",
        "pytest-catchlog>=1.2",
    ],
    cmdclass={"test": PyTest},
    zip_safe=False,
    keywords=" ".join(KEYWORDS),
    license="BSD License",
    url='https://github.com/kezabelle/django-debug-toolbar-urlconf-panel',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Framework :: Django",
        "Framework :: Django :: 1.4",
        "Framework :: Django :: 1.5",
        "Framework :: Django :: 1.6",
        "Framework :: Django :: 1.7",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)

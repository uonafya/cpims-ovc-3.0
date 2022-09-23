#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/swistakm/django-rest-framework/blob/master/rest_framework/runtests/runtests.py
import os
import sys

# fix sys path so we don't need to setup PYTHONPATH
os.environ['DJANGO_SETTINGS_MODULE'] = 'oauth_provider.runtests.settings'

import django
if django.VERSION >= (1, 7):
    django.setup()
from django.conf import settings
from django.test.utils import get_runner
if django.VERSION >= (1, 7):
    patch_for_test_db_setup = lambda: None
else:
    from south.management.commands import patch_for_test_db_setup


def usage():
    return """
    Usage: python runtests.py [UnitTestClass].[method]

    You can pass the Class name of the `UnitTestClass` you want to test.

    Append a method name if you only want to test a specific method of that class.
    """


def main():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2)

    if len(sys.argv) == 2:
        test_case = '.' + sys.argv[1]
    elif len(sys.argv) == 1:
        test_case = ''
    else:
        print(usage())
        sys.exit(1)

    patch_for_test_db_setup()

    if django.VERSION >= (1, 6):
        # due to some changes in Django>=1.6 test runner
        # if you not specify app then simply any `test` package
        # could be run e.g. `tests` provided by broken oauth2 package (sic!)
        test_prefix = 'oauth_provider.tests'
    else:
        # old test runner won't accept above prefix
        test_prefix = 'tests'

    failures = test_runner.run_tests([test_prefix + test_case])

    sys.exit(failures)

if __name__ == '__main__':
    main()

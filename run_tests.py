#!/usr/bin/env python
"""
Test runner script to help with test discovery issues in Jenkins.
This file helps resolve module import errors when running tests.
"""
import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    # Set up Django environment
    os.environ['DJANGO_SETTINGS_MODULE'] = 'static_site.settings'
    django.setup()
    
    # Create test runner
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # Run tests
    failures = test_runner.run_tests(["static_app.tests"])
    sys.exit(bool(failures))

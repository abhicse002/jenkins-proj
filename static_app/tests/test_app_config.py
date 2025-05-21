from django.test import TestCase
from django.apps import apps
from static_app.apps import StaticAppConfig


class AppConfigTest(TestCase):
    """Tests for app configuration"""

    def test_app_name(self):
        """Test that the app name is correct"""
        self.assertEqual(StaticAppConfig.name, 'static_app')

    def test_app_loaded(self):
        """Test that the app is loaded"""
        self.assertTrue(apps.is_installed('static_app'))
        self.assertTrue(apps.is_installed('django.contrib.staticfiles'))

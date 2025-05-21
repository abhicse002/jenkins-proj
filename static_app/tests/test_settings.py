from django.test import TestCase
from django.conf import settings


class SettingsTestCase(TestCase):
    """Tests for Django settings configuration"""

    def test_installed_apps(self):
        """Test that required apps are installed"""
        self.assertIn('static_app', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.staticfiles', settings.INSTALLED_APPS)

    def test_middleware(self):
        """Test that required middleware is installed"""
        self.assertIn('whitenoise.middleware.WhiteNoiseMiddleware', settings.MIDDLEWARE)

    def test_static_settings(self):
        """Test that static file settings are properly configured"""
        self.assertTrue(hasattr(settings, 'STATIC_URL'))
        self.assertTrue(hasattr(settings, 'STATICFILES_DIRS'))
        self.assertTrue(hasattr(settings, 'STATIC_ROOT'))

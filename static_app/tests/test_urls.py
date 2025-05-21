from django.test import SimpleTestCase
from django.urls import reverse, resolve
from static_app.views import home, about, contact


class UrlsTestCase(SimpleTestCase):
    """Test URL configuration for the static app"""

    def test_home_url_resolves(self):
        """Test that the home URL resolves to the correct view"""
        url = reverse('home')
        self.assertEqual(url, '/')
        self.assertEqual(resolve(url).func, home)

    def test_about_url_resolves(self):
        """Test that the about URL resolves to the correct view"""
        url = reverse('about')
        self.assertEqual(url, '/about/')
        self.assertEqual(resolve(url).func, about)

    def test_contact_url_resolves(self):
        """Test that the contact URL resolves to the correct view"""
        url = reverse('contact')
        self.assertEqual(url, '/contact/')
        self.assertEqual(resolve(url).func, contact)

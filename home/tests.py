"""
Home App - Tests
----------------

Test cases for Home App Routing
"""

from django.test import TestCase


class TestViews(TestCase):
    """
    Unit Tests for Home App Views

    UT1 - Test home page renders correct page
    UT2 - Test help page renders correct page
    """

    def test_home_page(self):
        """ UT01 - Test home page renders correct page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_help_page(self):
        """ UT02 - Test help page renders correct page """
        response = self.client.get('/help/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/help.html')

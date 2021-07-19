"""
Premium App - Tests
----------------

Test cases for Premium App Routing
"""

from django.test import TestCase


class TestViews(TestCase):
    def test_premium_page(self):
        """ Test premium page renders correct page """
        response = self.client.get('/premium/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/premium.html')

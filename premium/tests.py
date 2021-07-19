"""
Premium App - Tests
----------------

Test cases for Premium App Routing
"""

from django.test import TestCase
from django.conf import settings


class TestViews(TestCase):
    def test_premium_page(self):
        """ Test premium page renders correct page """
        response = self.client.get('/premium/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/premium.html')

    def test_stripe_config(self):
        """Test stripe public key view"""
        response = self.client.get('/premium/config/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                             {'publicKey': settings.STRIPE_PUBLISHABLE_KEY})

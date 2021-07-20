"""
Premium App - Tests
----------------

Test cases for Premium App Routing
"""

from django.test import TestCase
from django.conf import settings
import json
from profiles.models import Profile
from django.contrib.auth import get_user_model


class TestViews(TestCase):

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        pswd = "Kavanagh" # noqa
        email = "ben@ben.com"
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=pswd,
                                             email=email)
        logged_in = self.client.login(username=username, password=pswd)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)
        self.assertTrue(logged_in)

    def test_premium_page(self):
        """ Test premium page renders correct page """
        response = self.client.get('/premium/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/premium.html')

    def test_stripe_config(self):
        """ Test AJAX config view returns stripe public key """
        response = self.client.get('/premium/config/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                             {'publicKey': settings.STRIPE_PUBLISHABLE_KEY})

    def test_premium_checkout(self):
        """ Test AJAX checkout session view returns sessionId"""
        response = self.client.get('/premium/checkout/')
        json_response = json.loads(str(response.content, encoding='utf8'))
        self.assertTrue('sessionId' in json_response)

    def test_premium_checkout_error(self):
        """ Test AJAX checkout session view returns sessionId"""
        self.profile.paid = True
        self.profile.save()
        response = self.client.get('/premium/checkout/')
        json_response = json.loads(str(response.content, encoding='utf8'))
        self.assertTrue('error' in json_response)

    def test_success_page(self):
        """ Test successful payment page renders correct page """
        response = self.client.get('/premium/success/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/success.html')

    def test_abort_page(self):
        """ Test aborted payment page renders correct page """
        response = self.client.get('/premium/abort/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/abort.html')

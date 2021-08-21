"""
Premium App - Tests
----------------

Test cases for Premium App Routing
"""

import json
from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from profiles.models import Profile


class TestViews(TestCase):
    """
    Unit Tests for Premium App Views

    setUp - Create test login user and create Profile entry

    UT16 - Test premium page renders correct page
    UT17 - Test AJAX config view returns stripe public key
    UT18 - Test AJAX checkout session view returns sessionId
    UT19 - Test AJAX checkout returns error for premium users
    UT20 - Test successful payment page renders correct page
    UT21 - Test process invalid session_id redirects to premium
    UT22 - Test aborted payment page renders correct page
    """

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        pswd = "Kavanagh" # noqa
        email = "ben@ben.com"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username=username,
                                                   password=pswd,
                                                   email=email)
        logged_in = self.client.login(username=username, password=pswd)

        # Add User to Profile
        # Needed to be hardcoded as Profile signal uses email verification
        self.profile = Profile.objects.create(user=self.user)
        self.assertTrue(logged_in)

    def test_premium_page(self):
        """ UT16 - Test premium page renders correct page """
        response = self.client.get('/premium/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/premium.html')

    def test_stripe_config(self):
        """ UT17 - Test AJAX config view returns stripe public key """
        response = self.client.get('/premium/config/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),
                             {'publicKey': settings.STRIPE_PUBLISHABLE_KEY})

    def test_premium_checkout(self):
        """ UT18 - Test AJAX checkout session view returns sessionId """
        response = self.client.get('/premium/checkout/')
        json_response = json.loads(str(response.content, encoding='utf8'))
        self.assertTrue('sessionId' in json_response)

    def test_premium_checkout_error(self):
        """ UT19 - Test AJAX checkout returns error for premium users"""
        self.profile.paid = True
        self.profile.save()
        response = self.client.get('/premium/checkout/')
        json_response = json.loads(str(response.content, encoding='utf8'))
        self.assertTrue('error' in json_response)

    def test_success_page(self):
        """ UT20 - Test successful payment page renders correct page """
        # Navigate to premium
        self.client.get('/premium/')
        # Request checkout token/session
        self.client.get('/premium/checkout/')
        # Set payment success Token
        session = self.client.session
        session["SUCCESS_TOKEN"] = True
        session.save()
        # Navigate to Success page with overridden header
        response = self.client.get('/premium/success/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/success.html')

    def test_process_route(self):
        """ UT21 - Test process invalid session_id redirects to premium """
        # Test without param
        response = self.client.get('/premium/process/')
        self.assertEqual(response.status_code, 302)
        # Test with invalid param
        response = self.client.get('/premium/process/?session_id=1234')
        self.assertEqual(response.status_code, 302)

    def test_abort_page(self):
        """ UT22 - Test aborted payment page renders correct page """
        response = self.client.get('/premium/abort/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'premium/abort.html')

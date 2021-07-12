"""
Profiles App - Tests
----------------

Test cases for Profiles App Routing
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile
from codex.models import Codex


class TestViews(TestCase):

    # Load fixtures into test DB
    fixtures = ['codex.json']

    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "Ben"
        password = "Kavanagh"
        User = get_user_model()
        self.user = User.objects.create_user(username=username,
                                             password=password)
        logged_in = self.client.login(username=username, password=password)

        # Add User to Profile
        Profile.objects.create(user=self.user)

        # Test Login
        self.assertTrue(logged_in)

    def test_profile_context(self):
        """ Test Profile Context being passed to Profile page"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'][0].user, self.user)

    def test_create_context(self):
        """ Test Hero list Context being passed to Create page"""
        response = self.client.get('/profile/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.context['heroes'][0], Codex))
